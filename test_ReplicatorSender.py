import unittest
from unittest.mock import MagicMock, Mock
from ReplicatorSender import konekcija_klijent, konekcija_server, vise_klijenata,osnovni_podaci_sender
from unittest import mock

class TestReplicatorSender(unittest.TestCase):

    def test_osnovni_podaci_sender(self):
        with mock.patch('socket.socket') as mock_socket:
            mock_socket = Mock()
        mock_socket, _ = osnovni_podaci_sender(10002)

        self.assertEqual(mock_socket.getsockname(), ("127.0.0.1", 10002)) #provera da li je konekcija bila uspesna na portu
    
    def test_konekcija_server(self):
        _, indikator = konekcija_server(10003, "tip")
        self.assertEqual(indikator, 1)
        
    def test_konekcija_server_error(self):
        self.assertRaises(OverflowError, konekcija_server,10032132132103, "tip")
        
    def test_konekcija_klijent(self):
         _, indikator = konekcija_klijent(10003, "tip")
         self.assertEqual(indikator, 1) #posto nije doslo do konekcija baca se greska

        
    def test_konekcija_klijent_error(self):
        self.assertRaises(OverflowError, konekcija_klijent,10032132132103, "tip")
      
        
    def test_funkcija_klijent_sender(self):
        self.assertRaises(OverflowError,konekcija_klijent,12451245,"nesto")
        
    def test_vrednost_indikatora(self):
        self.assertIsNotNone(konekcija_klijent(10009,"nesto"))

   
    def test_vise_klijenata(self):
        with mock.patch('socket.socket') as mock_socket:
            mock_socket = Mock()
        vise_klijenata(mock_socket, mock_socket, "tip")

        promenljiva = mock_socket.recv.assert_called()
        self.assertIsNone(promenljiva)
        
    def test_konekcija_klijent2(self):
        self.assertIsNotNone(konekcija_klijent(10007,"tip"))
        
    def test_konekcija_server2(self):
        self.assertIsNotNone(konekcija_server(10007,"tip"))
    
 
if __name__=="__main__":
    unittest.main()