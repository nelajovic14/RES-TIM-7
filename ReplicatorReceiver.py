import select, socket
from ReplicatorKonekcija import konekcija_server, konekcija_klijent
from ReplicatorStrukturaITajmer import predefinisan_period
from ObradaPoruke import obrada
import time

def brisanje_iz_fajla(putanja):
    
    with open(putanja, 'w') as fajl:

        fajl.truncate(0)

    return time.time()

def upis_u_fajl(obradjena_poruka, putanja):
    with open(putanja,'a') as fajl:
        fajl.write(obradjena_poruka)
    return fajl

def citanje_iz_fajla(putanja):
    with open(putanja, 'r') as fajl:
        svi_redovi_fajla = fajl.readlines()
    return svi_redovi_fajla, len(svi_redovi_fajla), fajl

def obrada_primljene_poruke(replikator_poruka):
        obradjena_poruka = obrada(replikator_poruka) + '\n'
        print("Primljena poruka od replicator sender komponente: " + obradjena_poruka)
        return obradjena_poruka

def prijem_preko_mreze(soket_deskriptor):
    replikator_poruka = soket_deskriptor.recv(2048)
    replikator_poruka = replikator_poruka.decode("utf-8")
    return replikator_poruka

def prijem_upis_fajl(inputs, putanja):
    inputready,outputready,exceptready = select.select(inputs,[],[], 1.0)
    for s in inputready:
        replikator_poruka = prijem_preko_mreze(s)
        obradjena_poruka = obrada_primljene_poruke(replikator_poruka)
        upis_u_fajl(obradjena_poruka, putanja)
        return obradjena_poruka

def slanje_ka_readeru(tekst_fajl, reader_klijent):
    reader_aktivan = True
    data=""
    for line in tekst_fajl:
        try:
            data= reader_klijent.send(str.encode(line))
        except socket.error:
            reader_aktivan = False
            print("Reader server se ugasio")
            break
    return reader_aktivan,data, reader_klijent

def osnovni_podaci_i_konekcija(port_komunikacija):
    port_reader_komunikacije = 10003
    reader_aktivan = False
    putanja = "bafer.txt"
    naziv_komponente = "replicator-receiver"
    replikator_server,_ = konekcija_server(port_komunikacija, "replicator-receiver")
    return port_reader_komunikacije, reader_aktivan, putanja, naziv_komponente, replikator_server

def klijentska_uticnica(replikator_server, naziv_komponente):
    client, address = replikator_server.accept()
    print("[Klijent " + naziv_komponente + "] povezan sa adrese " + address[0] + ':' + str(address[1]))
    client.setblocking(0)
    inputs = [client]

    return inputs, client

def receiver():
    
    port_komunikacija = 10002

    port_reader_komunikacije, reader_aktivan, putanja, naziv_komponente, replikator_server = osnovni_podaci_i_konekcija(port_komunikacija)

   

    inputs,_ = klijentska_uticnica(replikator_server, naziv_komponente)



    while True:

        prijem_upis_fajl(inputs, putanja)



        if reader_aktivan == False:

            reader_klijent, indikator = konekcija_klijent(port_reader_komunikacije, "replicator-receiver")

            if indikator != 1:

                reader_aktivan = True

                start_time = time.time()

        else:

            if(int(time.time() - start_time) >= predefinisan_period):

                print("[Klijent " + naziv_komponente + "] proslo vreme: " + str(int(time.time() - start_time)))

                print("Prosledjivanje poruka ka reader serveru...")

                tekst_fajl, broj_redova, f = citanje_iz_fajla(putanja)

                reader_aktivan,_,_ = slanje_ka_readeru(tekst_fajl, reader_klijent)

                if reader_aktivan :

                    start_time = brisanje_iz_fajla(putanja)

if __name__=="__main__":
    receiver()