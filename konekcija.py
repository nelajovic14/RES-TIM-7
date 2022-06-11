from contextlib import nullcontext
import socket

class Konekcija:
    def __init__(self,port,ipaddress) :
        self.port=port
        self.ipaddress=ipaddress
    def connect(self):
        self.server_socket = socket.socket()
        server_socket=self.server_socket
        local_host = self.ipaddress
        port = self.port

        try:
            server_socket.bind((local_host, port))
        except socket.error as e:
            print(str(e))

        print("Waiting for a connection...")
        server_socket.listen(5)

        client, address = server_socket.accept()
        print("Connect to: " + address[0] + ":" + str(address[1]))

        self.client=client
        #poruka = client.recv(2048)       
        #poruka=poruka.decode("utf-8")
        #self.poruka=poruka
    def close(self):
        self.server_socket.close()
    def get_poruka(self):
        self.poruka=self.client.recv(2048)
        self.poruka=self.poruka.decode("utf-8")
        return self.poruka
            