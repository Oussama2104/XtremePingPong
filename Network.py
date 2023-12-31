import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "localhost"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getPlayer(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send(self, data):
        try:
            print("Sent data:", self.p)
            self.client.send(pickle.dumps(data))
            data = pickle.loads(self.client.recv(2048))
            print("Received data:", data)
            return data
        except socket.error as e:
            print(e)