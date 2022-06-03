from ReplicatorKonekcija import konekcijaKlijent, konekcijaServer
from ReplicatorStrukturaITajmer import *
import time

port_komunikacija = 10002
port_reader_komunikacija = 10003

replikator_klijent, replikator_server = konekcijaServer(port_komunikacija)
replikator_poruka = replikator_klijent.recv(2048)
replikator_poruka = replikator_poruka.decode("utf-8")

print("Primljena poruka od replicator sender komponente: " + replikator_poruka)

replikator_klijent.close()
replikator_server.close()

#sada se poruka prosledjuje na Reader, pa ce replicator receiver biti klijent koji salje paket ka reader serveru
reader_klijent = konekcijaKlijent(port_reader_komunikacija)
time.sleep(predefinisan_period) #ceka se 5 sekundi pre slanja podataka
reader_klijent.send(str.encode(replikator_poruka))
print("Poruka prosledjena ka Reader-u")

reader_klijent.close()