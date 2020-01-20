import asyncio
import re

DATA = {}
    

def answer_put(val):
    global DATA
    key, value, timestamp = val
    if key not in DATA:
        DATA[key] = [(int(timestamp), float(value))]
    else:
        DATA[key].append((int(timestamp), float(value)))
    return "ok\n\n"


def answer_get(key):
    global DATA
    print("DATA=", DATA)
    answer = "ok\n "
    if key == '*':
        for row in DATA:
            for subrow in DATA[row]:
                answer += '{} {} {}\n\n'.format(row, subrow[1], subrow[0])
        print(answer.encode())
        return answer
    elif key not in DATA:
        return answer.encode()
    
    for row in DATA[key]:
        answer += '{} {} {}\n\n'.format(key, row[1], row[0])
    print(answer.encode())
    return answer
        

def answer(value):
    s_val = value.split()
    print(s_val)
    if s_val[0] == 'put':
        return answer_put(s_val[1:])
    elif s_val[0] == 'get':
        return answer_get(s_val[1])
    
    return b"error\nwrong command"


async def handle(reader, writer):
    while True:
        print("start handle")
        data = await reader.read(1024)
        print("data=", data)
        if not data:
            break
        print("get reader")
        message = data.decode()
        addr = writer.get_extra_info("peername")
        print("message=", message)
        # writer.write(answer(message).encode())
        writer.write(b"\n\n")
    writer.close()
    print("close writer")


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(
        handle,
        host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == "__main__":
    run_server("127.0.0.1", 10001)
    