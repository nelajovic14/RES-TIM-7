import socket


def konekcija_klijent(broj_porta, tip_klijenta):
    client_socket = socket.socket()
    local_host = "127.0.0.1"
    indikator = 0

    print("[Klijent " + tip_klijenta + "] pokusavanje konekcije na port " + str(broj_porta))

    try:
        client_socket.connect((local_host, broj_porta))
        print("[Klijent " + tip_klijenta + "] konekcija na portu " + str(broj_porta) + " uspesna")
    except OverflowError:
        indikator=1
        raise OverflowError("Overflow port")
    except socket.error:
        #print("[Klijent " + tipKlijenta + "] server kojem se pristupa je nedostupan!")
        indikator = 1
       

    return client_socket, indikator

def vise_klijenata(connection, client_connection, tip_servera):
    while True:
        try:   
            data = connection.recv(2048)
            response = "[Server " + tip_servera + "] pristigla poruka: "  + data.decode('utf-8')
            print(response)
            client_connection.send(str.encode(response))
        except Exception:
            print("Konekcija writer-a ugasena")
            connection.close()
            break   

def konekcija_server(broj_porta, tip_servera):
    server_socket = socket.socket()
    local_host = "127.0.0.1"
    indikator=0

    try:
        server_socket.bind((local_host, broj_porta))
        indikator=1
    except OverflowError:
        raise OverflowError("Wrong port")  

    print("[Server " + tip_servera + "] osluskivanje klijentskih zahteva...")
    server_socket.listen(5)

    return server_socket,indikator



    