from ReplicatorKonekcija import konekcija_server, konekcija_klijent, vise_klijenata
from _thread import start_new_thread

def osnovni_podaci_sender(port_komunikacije):
    port_replicator_komunikacije = 10002
    server, _ = konekcija_server(port_komunikacije, "replicator-sender")
    return server, port_replicator_komunikacije


def sender():
    port_komunikacije = 10001
    server, port_replicator_komunikacije = osnovni_podaci_sender(port_komunikacije)
    while True:
        klijent_za_replicator, indikator = konekcija_klijent(port_replicator_komunikacije, "replicator-sender")
        if indikator != 1:
            break
        else:
            print("[Klijent replicator-sender] server kojem se pristupa je nedostupan!")
            print("Cekanje da se server aktivira...")

    while True:
        client, address = server.accept()
        print("Klijent povezan sa adrese " + address[0] + ':' + str(address[1]))
        start_new_thread(vise_klijenata, (client, klijent_za_replicator, "replicator-sender",))
    
    
if __name__=="__main__":
    sender()