import socket
import re

data_metrics = {}

def answer_put(value):
    global data_metrics
    try:
        _, key, value, timestamp = value.split()
        if key not in data_metrics:
            data_metrics[key] = [(float(value), int(timestamp)),]
        else:
            data_metrics[key].append((float(value), int(timestamp)))
        print(data_metrics)
        return b'ok\n\n'
    except:
        return b'error\nwrong command\n\n'    


def answer_get(value):
    global data_metrics
    _, key = value.split()
    try:
        return bytes(data_metrics[key])
    except:
        return bytes({})
            
        
def parser(value):
    
    if re.search('put.*\n', value):
        return answer_put(value)
    elif re.search('get.*\n', value):
        return answer_get(value)
    
def run_server(host, port):
    with socket.socket() as sock:
        sock.bind((host, port))
        sock.listen(1)
        while True:
            conn, addr = sock.accept()

            print('Соединение установлено:', addr)

            # переменная response хранит строку возвращаемую сервером, если вам для
            # тестирования клиента необходим другой ответ, измените ее
            response = b'ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n'

            while True:
                data = conn.recv(1024)
                if not data:
                    print("break", data)
                    break
                request = data.decode('utf-8')
                result = parser(request)
                if result:
                    response = result
                print("result=", result)
                print(f'Получен запрос: {ascii(request)}')
                # print(f'Отправлен ответ {ascii(response.decode("utf-8"))}')
                print(response)
                conn.send(response)

            conn.close()
            
            
if __name__ == "__main__":
    run_server("127.0.0.1", 10001)
        