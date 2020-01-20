import socket
import time

class Client:    
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = socket.create_connection((self.host, self.port), self.timeout)
        
    def socket(self):
        return self.sock
    
    def get(self, key):
        message = """get {key}\n""".format(key=key)
        try:
            with socket.create_connection((self.host, self.port), self.timeout) as sock:
                sock.send(message.encode("utf8"))
                answer = sock.recv(1024)
                print(answer)
                data = answer.decode().split('\n')
                metrics = {}
                if data[0] == 'ok':
                    for val in data[1:]:
                        if val != '':
                            key, value, timestamp = val.split()
                            if key not in metrics:
                                metrics[key] = [(int(timestamp), float(value))]
                            else:
                                metrics[key].append((int(timestamp), float(value)))
                    return metrics
                else:
                    return ClientError("client_get_error")
        
        except Exception as err:
            return ClientError(err)
    
    def put(self, key, value, timestamp=str(int(time.time()))):
        message = """put {key} {value} {timestamp}\n""".format(key=key, value=value, timestamp=timestamp)
        try:
            with socket.create_connection((self.host, self.port), self.timeout) as sock:
                sock.sendall(message.encode("utf8"))
                answer = sock.recv(1024)
                return answer.decode()
        except Exception as err:
            return ClientError(err)

    def _answer(self, val):
        print("+"*50)
        print("val=",val)
        print("-"*50)
    
    
class ClientError:
    def __init__(self, err):
        print(err)
        
        
if __name__ == "__main__":
    client = Client("127.0.0.1", 10001, timeout=2)
    client.put("qwe", 123, 312)
    client.get("qwe")