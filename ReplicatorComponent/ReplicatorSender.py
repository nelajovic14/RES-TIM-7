import ReplicatorStrukturaITajmer
from ReplicatorKonekcija import konekcijaServer, konekcijaKlijent
from ObradaPoruke import obrada

port_komunikacije = 10001
port_replicator_komunikacije = 10002

klijent, server = konekcijaServer(port_komunikacije)

poruka_od_writer = klijent.recv(2048)
poruka_od_writer = poruka_od_writer.decode("utf-8")

print("Primljena poruka od writer komponente: " + poruka_od_writer)
id, potrosnja, mesec, ime_korisnika, prezime_korisnika = obrada(poruka_od_writer)

korisnicki_zahtev = [id, potrosnja, mesec, ime_korisnika, prezime_korisnika]
ReplicatorStrukturaITajmer.privremeno_skladiste.append(korisnicki_zahtev)

print("Lista zahteva:")
for i in range(len(ReplicatorStrukturaITajmer.privremeno_skladiste)):
    print("Zahtev " + str(i) + ". ", end = ' ')
    for j in range(len(ReplicatorStrukturaITajmer.privremeno_skladiste[i])):
        if(j == len(ReplicatorStrukturaITajmer.privremeno_skladiste[i]) - 1):
            print (ReplicatorStrukturaITajmer.privremeno_skladiste[i][j] + " ")
        else:
            print (ReplicatorStrukturaITajmer.privremeno_skladiste[i][j] + " ", end = ' ')
        
        
klijent.close() 
server.close() #u funkciji nije zatvoren socket, pa mora ovde i to se radi na kraju komunikacije

#sada se ovaj replicator konektuje kao klijent na replicator sender koji ce biti server
replikator_klijent = konekcijaKlijent(port_replicator_komunikacije)
replikator_klijent.send(str.encode(poruka_od_writer))
print("Poruka prosledjena ka Replicator Receiver-u")

replikator_klijent.close()