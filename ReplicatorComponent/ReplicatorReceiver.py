import select, socket
from ReplicatorKonekcija import konekcijaKlijent, konekcijaServer
from ReplicatorStrukturaITajmer import *
from ObradaPoruke import obrada
import time

def upis_u_fajl(obradjena_poruka, putanja):
    fajl = open(putanja, "a")
    fajl.write(obradjena_poruka + "\n")
    fajl.close()

    return fajl

def prijem_upis_fajl(inputs, putanja):
    inputready,outputready,exceptready = select.select(inputs,[],[], 1.0)
    for s in inputready:
        replikator_poruka = s.recv(2048)
        replikator_poruka = replikator_poruka.decode("utf-8")

        obradjena_poruka = obrada(replikator_poruka)
        print("Primljena poruka od replicator sender komponente: " + obradjena_poruka)
   
        f = upis_u_fajl(obradjena_poruka, putanja)

def receiver():
    port_komunikacija = 10002
    port_reader_komunikacije = 10003
    reader_aktivan = False
    putanja = "ReplicatorComponent/bafer.txt"
    naziv_komponente = "replicator-receiver"

    replikator_server = konekcijaServer(port_komunikacija, "replicator-receiver")

    client, address = replikator_server.accept()
    print("[Klijent " + naziv_komponente + "] povezan sa adrese " + address[0] + ':' + str(address[1]))
    client.setblocking(0)
    inputs = [client]

    while True: 
        prijem_upis_fajl(inputs, putanja)

        if reader_aktivan == False:
            reader_klijent, indikator = konekcijaKlijent(port_reader_komunikacije, "replicator-receiver")
            if indikator != 1:
                reader_aktivan = True
                start_time = time.time()
        else:
            if(int(time.time() - start_time) >= predefinisan_period):
                print("[Klijent " + naziv_komponente + "] proslo vreme: " + str(int(time.time() - start_time)))
                print("Prosledjivanje poruka ka reader serveru...")
                f = open(putanja, "r")
                for line in f:
                    try:
                        reader_klijent.send(str.encode(line))
                    except socket.error:
                        reader_aktivan = False
                        print("Reader server se ugasio")
                        break

                if reader_aktivan :
                    f.close()
                    f = open(putanja, "a")
                    f.truncate(0)
                    f.close()
                    start_time = time.time()
                else:
                    f.close()

receiver()