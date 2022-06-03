import socket

def konekcijaKlijent(brojPorta):
    clientSocket = socket.socket()
    localHost = "127.0.0.1"
    port = brojPorta

    print("Cekanje na konekciju")

    try:
        clientSocket.connect((localHost, port))
        print("Konekcija na portu " + str(port) + " uspesna")
    except socket.error as e:
        print(str(e))

    return clientSocket

    #clientSocket.send(str.encode(poruka))
    #print("Klijent uspesno poslao ID")

    #clientSocket.close()

def konekcijaServer(brojPorta):
    serverSocket = socket.socket()
    localHost = "127.0.0.1"
    port = brojPorta

    try:
        serverSocket.bind((localHost, port))
    except socket.error as e:
        print(str(e))

    print("Waiting for a connection...")
    serverSocket.listen(5)

    client, address = serverSocket.accept()
    print("Konektovano na: " + address[0] + ":" + str(address[1]))
    return client, serverSocket



    