import socket

serverSocket = socket.socket()
localHost = "127.0.0.1"
port = 10002

try:
    serverSocket.bind((localHost, port))
except socket.error as e:
    print(str(e))

print("Waiting for a connection...")
serverSocket.listen(5)

client, address = serverSocket.accept()
print("Connect to: " + address[0] + ":" + str(address[1]))

poruka = client.recv(2048)
poruka=poruka.decode("utf-8")
print("Server primio poruku od klijenta " + poruka)

def konekcija(poruka):
    clientSocket = socket.socket()
    localHost = "127.0.0.1"
    port = 10003

    print("Waiting for connection")

    try:
        clientSocket.connect((localHost, port))
    except socket.error as e:
        print(str(e))


    clientSocket.send(str.encode(poruka))
    print("Klijent uspesno poslao ID")


    clientSocket.close()

konekcija(poruka)