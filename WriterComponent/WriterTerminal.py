from email import message
import socket
from WriterClass import Message

def unosPodataka():
    print("---- Unos novih podataka ---- ") 
    print("Unesite ID korisnika: ")
    id = input()

    print("Unesite trenutnu potrosnju vode korisnika: ")
    potrosnja = input()

    Message.__init__(message, id, potrosnja)
    return message



def konekcija():
    clientSocket = socket.socket()
    localHost = "127.0.0.1"
    port = 10001

    print("Waiting for connection")

    try:
        clientSocket.connect((localHost, port))
    except socket.error as e:
        print(str(e))

    message = unosPodataka()

    clientSocket.send(str.encode(Message.__str__(message)))
    print("Klijent uspesno poslao ID")


    clientSocket.close()


konekcija()

