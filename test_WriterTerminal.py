from distutils.log import Log
import unittest
from unittest import expectedFailure, mock
from urllib import response
from WriterComponent.Konekcija_client import KonekcijaClient
from WriterComponent.WriterTerminal import logovanje, splitovanje, otvori_fajl,provera_ispravnosti_podataka, unos_podataka
from WriterComponent.WriterClass import Message
from unittest.mock import Mock,patch, MagicMock

class TestWriter(unittest.TestCase):
    @patch('builtins.input')
    def test_logovanje(self,input_log):
        input_log.side_effect=["Marko123","12345"]
        expected_from_logovanje=("Marko","Markovic")
        response_from_logovanje=logovanje()
        self.assertEqual(expected_from_logovanje,response_from_logovanje)
        
    @patch('builtins.input')
    def test_logovanje2(self,input_log):
        input_log.side_effect=["Jeca","123321"]
        expected_from_logovanje=("Jelena","Jovanovic")
        response_from_logovanje=logovanje()
        self.assertEqual(expected_from_logovanje,response_from_logovanje)
        
    @patch('builtins.input')
    def test_logovanje3(self,input_log):
        input_log.side_effect=["MilicaMilic","nekaSifra11"]
        expected_from_logovanje=("Milica","Milic")
        response_from_logovanje=logovanje()
        self.assertEqual(expected_from_logovanje,response_from_logovanje)
        
    @patch('builtins.input')
    def test_logovanje4(self,input_log):
        input_log.side_effect=["Jovann","988777"]
        expected_from_logovanje=("Jovan","Jovic")#sta ocekujemo da bi ta fja trebala da vrati
        response_from_logovanje=logovanje() #ono sto ce fja zapravo vratiti
        self.assertEqual(expected_from_logovanje,response_from_logovanje)#ako je to sto fja vrati jednako onome sto smo 
        #ocekivali taj test ce da prodje
        
    @patch('builtins.input')#kad je neki pogresan unos, onda smo stavili da vraca prazan string     
    def test_logovanje_false(self,input_value):
        input_value.side_effect=["nn","12345"]#ako je korisnik pogresio ime
        expected_from_logovanje=("","")
        response_from_logovanje=logovanje()
        self.assertEqual(expected_from_logovanje,response_from_logovanje)
        
    @patch('builtins.input')   
    def test_logovanje_false1(self,input_value):
        input_value.side_effect=["Marko123","nn"]#ako je korisnik pogresio sifru
        expected_from_logovanje=("","")#kad unesemo pogresno ocekujemo da ce se vratiti
        response_from_logovanje=logovanje()
        self.assertEqual(expected_from_logovanje,response_from_logovanje)
        
    @patch('builtins.input')    
    def test_logovanje_false2(self,input_value):
        input_value.side_effect=["nn","nn"]#ako je pogresio i jedno i drugo
        expected_from_logovanje=("","")
        response_from_logovanje=logovanje()
        self.assertEqual(expected_from_logovanje,response_from_logovanje)        
    
    
    
    ################################  Unos podataka  ##################################################
    @patch('builtins.input')  
    def test_unos_podataka(self,input_values):#ispravan unos(proverimo samo da li nam vraca objekat tog tipa)
        input_values.side_effect=["5","500","april"]#to smo kao uneli sa konzole
        response_from_unos_podataka=unos_podataka("Marko","Markovic");
        self.assertIsInstance(response_from_unos_podataka,Message)#uporedimo da li vraca dobar tip klase
            
    @patch('builtins.input')  #proveravamo da li vraca dobre vrednosti
    def test_unos_podataka1(self,input_values):
        input_values.side_effect=["5","600","april"]
        response_from_unos_podataka=unos_podataka("Marko","Markovic");

        mess=Message("5","600","april","Marko","Markovic")
        
        
        self.assertEqual(response_from_unos_podataka.id, mess.id)
        self.assertEqual(response_from_unos_podataka.potrosnja, mess.potrosnja)
        self.assertEqual(response_from_unos_podataka.mesec, mess.mesec)
        self.assertEqual(response_from_unos_podataka.korisnik_ime, mess.korisnik_ime)
        self.assertEqual(response_from_unos_podataka.korisnik_prezime, mess.korisnik_prezime)
    
    
    def test_ispis_klase(self):
        ispis = MagicMock(return_value ="Server primio podatke od korisnika: "+ "Marko" + " " +  "Markovic" + "\n" +"id:" + " "+ "1" + "\n" + "potrošnja: "  + ""+ "500" + "\n" + "mesec: " + "april")
        mess=Message("1","500","april","Marko","Markovic")
        self.assertEquals(ispis(),mess.__str__())
        
        
    def test_unoss(self):
        id_korisnika = "5"
        potrosnja = "600"
        mesec = "maj"
        ocekivanje = True
        odg = provera_ispravnosti_podataka(id_korisnika, potrosnja, mesec)
        self.assertEqual(ocekivanje, odg)   
    
    def test_unoss1(self):
        id_korisnika = "kdsfjdskhd"
        potrosnja = "600"
        mesec = "maj"
        ocekivanje = False
        odg = provera_ispravnosti_podataka(id_korisnika, potrosnja, mesec)
        self.assertEqual(ocekivanje, odg)  
        
    def test_unoss2(self):
        id_korisnika = "5"
        potrosnja = "kkk"
        mesec = "jun"
        ocekivanje = False
        odg = provera_ispravnosti_podataka(id_korisnika, potrosnja, mesec)
        self.assertEqual(ocekivanje, odg)
               
    def test_unoss3(self):
        id_korisnika = "5"
        potrosnja = "600"
        mesec = "kakaka"
        ocekivanje = False
        odg = provera_ispravnosti_podataka(id_korisnika, potrosnja, mesec)
        self.assertEqual(ocekivanje, odg)       
    def test_splitovanje(self):
        linija = "Marko Markovic Marko123 12345"
        expected_response = ("Marko", "Markovic", "Marko123", "12345")
        response = splitovanje(linija)
        self.assertEqual(response, expected_response)
        
        
    def test_greska(self):
        linija = "MarkoMarkovic Marko 12345"
        self.assertRaises(IndexError, splitovanje, linija)
    def test_greska1(self):
        linija = "MarkoMarkovic Marko"
        self.assertRaises(IndexError, splitovanje, linija)
        
    def test_greska2(self):
        linija = "MarkoMarkovic"
        self.assertRaises(IndexError, splitovanje, linija)
    
    def test_greska3(self):
        linija = ""
        self.assertRaises(IndexError, splitovanje, linija)
        
    def test_fajl(self):
        odg = "korisnicci.txt"
        response = otvori_fajl(odg)
        ocekivanje = -1
        self.assertEqual(ocekivanje, response)
  
    def test_connection(self):
        conn=KonekcijaClient(10008,'127.0.0.1')
        self.assertIsInstance(conn,KonekcijaClient)
  
    def test_connection_send(self):
        mock_connect=Mock()
        poruka="hello"
        KonekcijaClient.send(mock_connect,poruka)
        mock_connect.client_socket.send.assert_called()
        mock_connect.client_socket.close()
        
    def test_connection_close(self):
        mock_connect=Mock()
        KonekcijaClient.close(mock_connect)
        mock_connect.server_socket.close.assert_called()
        mock_connect.server_socket.close()     
        
    
if __name__=="__main__":
    unittest.main(verbosity=2,exit=False)