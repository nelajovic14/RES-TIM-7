import socket


class KonekcijaClient:
    def __init__(self,port,ipaddress) :
        self.ipaddress=ipaddress
        self.port=port
    def connect(self):
        self.client_socket = socket.socket()

        print("Waiting for connection")

        try:
            self.client_socket.connect((self.ipaddress, self.port))
        except socket.error as e:
            print(str(e))
    def send(self,poruka):
        self.client_socket.send(str.encode(poruka))
    def close(self):
        try:
            self.server_socket.close()
        except socket.error as e:
            print(str(e))