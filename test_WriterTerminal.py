from distutils.log import Log
from io import TextIOWrapper
import unittest
from unittest import expectedFailure, mock
from urllib import response
from KonekcijaWriter import KonekcijaClient
from WriterTerminal import logovanje, splitovanje, otvori_fajl,provera_ispravnosti_podataka, unos_podataka
from WriterClass import Message
from unittest.mock import Mock,patch, MagicMock

class TestWriter(unittest.TestCase):
    @patch('builtins.input')
    def test_logovanje(self,input_log):
        input_log.side_effect=["Marko123","12345"]
        expected_from_logovanje=("Marko","Markovic")
        response_from_logovanje=logovanje()
        self.assertEqual(expected_from_logovanje,response_from_logovanje)
        
    @patch('builtins.input')
    def test_logovanje1(self,input_log):
        input_log.side_effect=["Jeca","123321"]
        expected_from_logovanje=("Jelena","Jovanovic")
        response_from_logovanje=logovanje()
        self.assertEqual(expected_from_logovanje,response_from_logovanje)
        
    @patch('builtins.input')
    def test_logovanje2(self,input_log):
        input_log.side_effect=["MilicaMilic","nekaSifra11"]
        expected_from_logovanje=("Milica","Milic")
        response_from_logovanje=logovanje()
        self.assertEqual(expected_from_logovanje,response_from_logovanje)
        
    @patch('builtins.input')
    def test_logovanje3(self,input_log):
        input_log.side_effect=["Jovann","988777"]
        expected_from_logovanje=("Jovan","Jovic")
        response_from_logovanje=logovanje() 
        self.assertEqual(expected_from_logovanje,response_from_logovanje)
        
    @patch('builtins.input')     
    def test_logovanje_pogresno_ime(self,input_value):
        input_value.side_effect=["nn","12345"]
        expected_from_logovanje=("","")
        response_from_logovanje=logovanje()
        self.assertEqual(expected_from_logovanje,response_from_logovanje)
        
    @patch('builtins.input')   
    def test_logovanje_pogresna_sifra(self,input_value):
        input_value.side_effect=["Marko123","nn"]
        expected_from_logovanje=("","")
        response_from_logovanje=logovanje()
        self.assertEqual(expected_from_logovanje,response_from_logovanje)
        
          
    @patch('builtins.input')  
    def test_unos_podataka(self,input_values):
        input_values.side_effect=["5","500","april"]
        response_from_unos_podataka=unos_podataka("Marko","Markovic");
        self.assertIsInstance(response_from_unos_podataka,Message)
            
    @patch('builtins.input')  
    def test_unos_ispravnih_podataka(self,input_values):
        input_values.side_effect=["5","600","april"]
        response_from_unos_podataka=unos_podataka("Marko","Markovic");

        mess=Message("5","600","april","Marko","Markovic")
        
        
        self.assertEqual(response_from_unos_podataka.id , mess.id)
        self.assertEqual(response_from_unos_podataka.potrosnja, mess.potrosnja)
        self.assertEqual(response_from_unos_podataka.mesec, mess.mesec)
        self.assertEqual(response_from_unos_podataka.korisnik_ime, mess.korisnik_ime)
        self.assertEqual(response_from_unos_podataka.korisnik_prezime, mess.korisnik_prezime)
    
    
    def test_ispis_klase(self):
        ispis = MagicMock(return_value ="Server primio podatke od korisnika: "+ "Marko" + " " +  "Markovic" + "\n" +"id:" + " "+ "1" + "\n" + "potrošnja: "  + ""+ "500" + "\n" + "mesec: " + "april")
        mess=Message("1","500","april","Marko","Markovic")
        self.assertEquals(ispis(),mess.__str__())
            
    def test_ispravnost_unetih_podataka(self):
        id_korisnika = "5"
        potrosnja = "600"
        mesec = "maj"
        ocekivanje = True
        odg = provera_ispravnosti_podataka(id_korisnika, potrosnja, mesec)
        self.assertEqual(ocekivanje, odg)   
    
    def test_neispravan_id(self):
        id_korisnika = "kdsfjdskhd"
        potrosnja = "600"
        mesec = "maj"
        ocekivanje = False
        odg = provera_ispravnosti_podataka(id_korisnika, potrosnja, mesec)
        self.assertEqual(ocekivanje, odg)  
        
    def test_neispravna_potrosnja(self):
        id_korisnika = "5"
        potrosnja = "kkk"
        mesec = "jun"
        ocekivanje = False
        odg = provera_ispravnosti_podataka(id_korisnika, potrosnja, mesec)
        self.assertEqual(ocekivanje, odg)
               
    def test_neispravan_mesec(self):
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
        
        
    def test_splitovanje_greska(self):
        linija = "MarkoMarkovic Marko 12345"
        self.assertRaises(IndexError, splitovanje, linija)
        
    def test_splitovanje_greska1(self):
        linija = "MarkoMarkovic Marko"
        self.assertRaises(IndexError, splitovanje, linija)
        
    def test_splitovanje_greska2(self):
        linija = "MarkoMarkovic"
        self.assertRaises(IndexError, splitovanje, linija)
    
    def test_splitovanje_greska3(self):
        linija = ""
        self.assertRaises(IndexError, splitovanje, linija)
        
    def test_nepostojeci_fajl(self):
        odg = "fajl.txt"
        response = otvori_fajl(odg)
        ocekivanje = -1
        self.assertEqual(ocekivanje, response)
    
    def test_uspesno_otvoren_fajl(self):
       
        otvoreni_fajl = otvori_fajl("korisnici.txt")
        self.assertIsInstance(otvoreni_fajl, TextIOWrapper) 
        otvoreni_fajl.close()
       
    def test_connection(self):
        conn=KonekcijaClient(10008,'127.0.0.1')
        self.assertIsInstance(conn,KonekcijaClient)
  
    def test_connection_send(self):
        mock_connect=Mock()
        
        KonekcijaClient.send(mock_connect,"Neka poruka")
        mock_connect.client_socket.send.assert_called()
        mock_connect.client_socket.close()
        
   
         
    
if __name__=="__main__":
    unittest.main(verbosity=2,exit=False)