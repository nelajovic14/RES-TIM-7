from ReplicatorKonekcija import konekcijaServer, konekcijaKlijent, vise_klijenata
from _thread import *

def sender():
    port_komunikacije = 10001
    port_replicator_komunikacije = 10002
    brojac_niti = 0

    server = konekcijaServer(port_komunikacije, "replicator-sender")
    while True:
        klijent_za_replicator, indikator = konekcijaKlijent(port_replicator_komunikacije, "replicator-sender")
        if indikator != 1:
            break
        else:
            print("[Klijent replicator-sender] server kojem se pristupa je nedostupan!")
            print("Cekanje da se server aktivira...")

    while True:
        client, address = server.accept()
        print("Klijent povezan sa adrese " + address[0] + ':' + str(address[1]))
        start_new_thread(vise_klijenata, (client, klijent_za_replicator, "replicator-sender",))
        brojac_niti += 1
        print('Broj aktivnih niti: ' + str(brojac_niti))

sender()