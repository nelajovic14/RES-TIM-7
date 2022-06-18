from contextlib import nullcontext
from ctypes import WinError
from math import e
import socket

class Konekcija:
    def __init__(self,port,ipaddress) :  
        try:
            int(port)
        except ValueError:
            raise ValueError("Pogresna port")  
        self.port=port
        self.ipaddress=ipaddress
    def bind_socket(self,ipaddress,port):
        self.server_socket = socket.socket()

        try:
            self.server_socket.bind((ipaddress, port))
        except OSError:
            raise OSError("WinError")
        except OverflowError:
            raise OverflowError("Wrong port")  
    def connect(self):    
        print("Waiting for a connection...")
        self.server_socket.listen(5)       

        client, address = self.server_socket.accept()
        print("Connect to: " + address[0] + ":" + str(address[1]))

        self.client=client
    
    def get_poruka(self):
        self.poruka=self.client.recv(2048)
        self.poruka=self.poruka.decode("utf-8")
        return self.poruka
            