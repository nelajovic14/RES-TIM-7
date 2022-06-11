import socket


def konekcijaKlijent(brojPorta, tipKlijenta):
    clientSocket = socket.socket()
    localHost = "127.0.0.1"
    indikator = 0

    print("[Klijent " + tipKlijenta + "] pokusavanje konekcije na port " + str(brojPorta))

    try:
        clientSocket.connect((localHost, brojPorta))
        print("[Klijent " + tipKlijenta + "] konekcija na portu " + str(brojPorta) + " uspesna")
    except socket.error as e:
        #print("[Klijent " + tipKlijenta + "] server kojem se pristupa je nedostupan!")
        indikator = 1

    return clientSocket, indikator

def vise_klijenata(connection, clientConnection, tipServera):
    while True:
        try:   
            data = connection.recv(2048)
            response = "[Server " + tipServera + "] pristigla poruka: "  + data.decode('utf-8')
            print(response)
            clientConnection.send(str.encode(response))
        except ConnectionResetError:
            print("Konekcija writer-a ugasena")
            connection.close()
            break   

def konekcijaServer(brojPorta, tipServera):
    serverSocket = socket.socket()
    localHost = "127.0.0.1"

    try:
        serverSocket.bind((localHost, brojPorta))
    except socket.error as e:
        print(str(e))

    print("[Server " + tipServera + "] osluskivanje klijentskih zahteva...")
    serverSocket.listen(5)

    return serverSocket



    