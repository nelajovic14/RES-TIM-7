from pydoc import cli
import unittest
from unittest import mock
from unittest.mock import patch, mock_open, Mock,MagicMock
from ReplicatorReceiver import brisanje_iz_fajla, upis_u_fajl, citanje_iz_fajla, obrada_primljene_poruke, prijem_preko_mreze, prijem_upis_fajl, slanje_ka_readeru, osnovni_podaci_i_konekcija, klijentska_uticnica
from ObradaPoruke import obrada
from ReplicatorKonekcija import konekcija_server, konekcija_klijent, vise_klijenata
import socket
soket_ime = 'socket.socket'
lazna_putanjaa = "fake/file/path"
receiver_otvaranje ='ReplicatorReceiver.open'
class TestReplicatorReceiver(unittest.TestCase):
    
    def test_primanje_preko_mreze(self):
        with mock.patch(soket_ime) as mock_socket:
            mock_socket = Mock()
        prijem_preko_mreze(mock_socket)
        mock_socket.recv.assert_called()
        mock_socket.close()

    def test_osnovni_podaci_konekcija(self):
        _, _, _, _, mock_socket = osnovni_podaci_i_konekcija(10002)

        self.assertEqual(mock_socket.getsockname(), ("127.0.0.1", 10002)) #provera da li je konekcija bila uspesna na portu
        mock_socket.close()


        
    def test_prijem_upis_fajl(self):
        soket = socket.socket()
        lazna_putanja = lazna_putanjaa
        self.assertIsNone(prijem_upis_fajl([soket], lazna_putanja))
        soket.close()
        
    

    def test_slanje_ka_readeru(self):

        mock_sockett = "ne prosledi se uticnica da bi se isprovocirao exception"

        lazni_tekst = "tekst\tekst\n\n"

        with self.assertRaises(Exception):

            slanje_ka_readeru(lazni_tekst, mock_sockett)

           
        socket1 = socket.socket()

        socket2 = socket.socket()

        dataa = 0



        socket2.bind(("127.0.0.1", 10003))

        socket2.listen(5)

        socket1.connect(("127.0.0.1", 10003))

       

        mock_socket, _ = socket2.accept()



        for line in lazni_tekst:

            dataa = mock_socket.send(str.encode(line))

        _, data, socket_klijenta = slanje_ka_readeru(lazni_tekst, mock_socket)

   

        self.assertEqual(dataa, data)

       

        socket1.close()

        socket2.close()

        mock_socket.close()
        socket_klijenta.close()
        
    def test_fajl_brisanje(self):
        lazna_putanja = lazna_putanjaa
        m = mock_open()

        with patch(receiver_otvaranje, m) as mokovan_fajl:

           brisanje_iz_fajla(lazna_putanja)

           mokovan_fajl.assert_called_once_with(lazna_putanja, 'w')


    
    def test_fajl_pisanje(self):
        lazna_putanja = lazna_putanjaa
        sadrzaj = "Message to write on file to be written"
        m = mock_open()
        with patch(receiver_otvaranje, m) as mokovan_fajl:
           upis_u_fajl(sadrzaj, lazna_putanja)
           mokovan_fajl.assert_called_once_with(lazna_putanja, 'a')
           mokovan_fajl().write.assert_called_once_with(sadrzaj)

    def test_fajl_citanje(self):
        sadrzaj = """Neki sadrzaj
        neki novi sadrzaj
        red 3
        red 4"""
        lazna_putanja = lazna_putanjaa
        m = mock_open(read_data = sadrzaj)

        with patch(receiver_otvaranje, m) as mokovan_fajl:
            vraceni_sadrzaj, broj_linija, fajl = citanje_iz_fajla(lazna_putanja)
            mokovan_fajl.assert_called_once_with(lazna_putanja, 'r')
            broj_linija_test = len(sadrzaj.split('\n'))
        
            self.assertEqual(broj_linija, broj_linija_test)
        
    def test_uspesna_obrada(self):
        test_poruka = "Server primio podatke od korisnika: Nebitni Nebitnic\nid: 1\npotrošnja: 2\nmesec: januar"
        
        povratna_obrada = obrada(test_poruka) + '\n'
        povratna_prijem_upis_fajl = obrada_primljene_poruke(test_poruka) 

        self.assertEqual(povratna_obrada, povratna_prijem_upis_fajl)
        
    def test_obrada(self):
        ulazna_poruka = "Server primio podatke od korisnika: Nebitni Nebitnic\nid: 1\npotrošnja: 2\nmesec: januar"
        povratna_poruka = "1, 2, januar"
        self.assertEqual(obrada(ulazna_poruka), povratna_poruka)
    def test_exception(self):
        poruka=",,nestp"
        self.assertRaises(IndexError,obrada,poruka)
        
    def test_konekcija_server(self):
        server_socket, indikator = konekcija_server(10003, "tip")
        self.assertEqual(indikator, 1)
        server_socket.close()
        
        
    def test_konekcija_server_error(self):
        self.assertRaises(OverflowError, konekcija_server,10032132132103, "tip")

    def test_konekcija_klijent(self):
        client_socket, indikator = konekcija_klijent(10003, "tip")
        self.assertEqual(indikator, 1) 
        client_socket.close()

    def test_vise_klijenata(self):
        with mock.patch(soket_ime) as mock_socket:
            mock_socket = Mock()
        vise_klijenata(mock_socket, mock_socket, "tip")
        

        promenljiva = mock_socket.recv.assert_called()
        self.assertIsNone(promenljiva)
        mock_socket.close()
        
    def test_konekcija_klijent3(self):
       client_socket, indikator = konekcija_klijent(10003, "tip")

       self.assertIsNotNone((client_socket, indikator))

       client_socket.close()
        
        
        
    
if __name__=="__main__":
    unittest.main()