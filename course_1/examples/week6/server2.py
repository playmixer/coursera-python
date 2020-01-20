import asyncio

DATA = {}

class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = data.decode()
        print(resp)
        _answer = self.answer(resp).encode("utf-8")
        print(_answer)
        self.transport.write(_answer)
        
    def answer_put(self, val):
        if len(val) < 3:
            return 'error\nkey cannot contain *\n\n'
        global DATA
        key, value, timestamp = val
        if key not in DATA:
            DATA[key] = [(int(timestamp), float(value))]
        if not (int(timestamp), float(value)) in DATA[key]:            
            DATA[key].append((int(timestamp), float(value)))
        DATA[key].sort(key=lambda x: x[0])
        print(DATA[key])
        return "ok\n\n"

    def answer_get(self, key):
        global DATA
        # print("DATA=", DATA)
        answer = "ok\n"
        if key == '*':
            for row in DATA:
                for subrow in DATA[row]:
                    answer += '{} {} {}\n'.format(row, subrow[1], subrow[0])
        elif key in DATA:
            for row in DATA[key]:
                answer += '{} {} {}\n'.format(key, row[1], row[0])
        print(answer.encode())
        return answer + '\n'
            

    def answer(self, value):
        s_val = value.split()
        print(s_val)
        if s_val[0] == 'put':
            return self.answer_put(s_val[1:])
        elif s_val[0] == 'get':
            return self.answer_get(s_val[1])
        
        return "error\nwrong command\n\n"


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
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