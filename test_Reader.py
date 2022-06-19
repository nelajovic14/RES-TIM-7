from contextlib import nullcontext
from ctypes import WinError
import ipaddress
from sqlite3 import DatabaseError
from threading import local
from typing import Type
import unittest
from unittest import mock
from unittest import result
from Reader import konekcija, splitovanje_parametara_za_bazu,provera_id,upis_u_bazu,connection_string,cx_Oracle
from KonekcijaKaBazi import Baza
from konekcija import Konekcija
from unittest.mock import MagicMock, Mock,patch
  
class TestReader(unittest.TestCase):
    def test_parametri(self):
        excepted_response=splitovanje_parametara_za_bazu("5,85,jun")
        right_response=(5,85,'jun')
        self.assertEqual(excepted_response,right_response)
    
    def test_with_wrong_id(self):
        self.assertRaises(ValueError,splitovanje_parametara_za_bazu,"l,25,jul")
    def test_with_wrong_potrosnja(self):
        self.assertRaises(ValueError,splitovanje_parametara_za_bazu,"5,kl,jul")
    def test_with_wrong_both(self):
        self.assertRaises(ValueError,splitovanje_parametara_za_bazu,"l,kl,jul")
    def test_with_wrong_commas(self):
        self.assertRaises(IndexError,splitovanje_parametara_za_bazu,"5,12")
    def test_with_wrong_commas2(self):
        self.assertRaises(IndexError,splitovanje_parametara_za_bazu,"8")
    def test_with_wrong_commas3(self):
        self.assertRaises(IndexError,splitovanje_parametara_za_bazu,"")
      
    def test_provera_id(self):
        self.assertEqual(False,provera_id(5,"jul"))
    def test_provera_id2(self):
        self.assertEqual(False,provera_id(1,"jun"))
    def test_provera_id3(self):
        self.assertEqual(True,provera_id(1,"jul"))
        
    def test_upis_u_bazu(self):
        mock_print=mock.Mock(side_effect=lambda:(print("Upisan je podatak u bazu!")))
        self.assertEqual(mock_print(),upis_u_bazu(1,12,'april',connection_string))
    def test_upis_u_bazu_false(self):
        mock_print=mock.Mock(side_effect=lambda:(print("Pdataka nije upisan u bazu!")))
        self.assertEqual(mock_print(),upis_u_bazu(5,12,'april',connection_string))
    def test_query(self):
        baza=Baza(connection_string)
        self.assertRaises(cx_Oracle.DatabaseError,baza.do_query,"INSERT INTO POTROSNJAKORISNIKA VALUES (5,5,\'jun\')")
    def test_query_with_parameters(self):
        baza=Baza(connection_string)
        self.assertIsNotNone(baza.do_query_with_result("select count(*) from BROJILO"))
    def test_query_with_parameters2(self):
        baza=Baza(connection_string)
        self.assertIsNotNone(baza.do_query_with_result("select IME from BROJILO where Idb=1"))
    def test_query_with_parameters3(self):
        baza=Baza(connection_string)
        self.assertRaises(cx_Oracle.DatabaseError,baza.do_query_with_result,"select IME from BROJILO where Idbrojila=10")
    def test_query_with_parameters4(self):
        baza=Baza(connection_string)
        self.assertRaises(cx_Oracle.DatabaseError,baza.do_query_with_result,"select MESEC from POTROSNJAKORISNIKA where Idb=5")
    def test_query_with_parameters5(self):
        baza=Baza(connection_string)
        self.assertAlmostEqual(baza.do_query_with_result("select IME from BROJILO where Idb=5"),[])
    def test_execute(self):
        query="INSERT INTO POTROSNJA VALUES (555,1,50,\'novembar\')"
        mock_baza=Mock()
        Baza.do_query(mock_baza,query)
        mock_baza.connection.cursor().execute.assert_called_with(query)

    def test_connection_recv(self):
        mock_connect=Mock()
        Konekcija.get_poruka(mock_connect)
        mock_connect.client.recv.assert_called()
        mock_connect.server_socket.close()
        mock_connect.client.close()
        
    
        
   
    def test_connection_ipaddress(self):
        connection=Konekcija(10007,"122.0.0.1")
        self.assertRaises(OSError,connection.bind_socket,'122.0.0.1',10007)
        connection.server_socket.close()
        
    def test_connection_port(self):
        connection=Konekcija(9999999,"127.0.0.1")
        self.assertRaises(OverflowError,connection.bind_socket,'127.0.0.1',99999999999)
        connection.server_socket.close()
    
    def test_connection_port_type(self):
        konekcija=nullcontext
        self.assertRaises(ValueError,Konekcija.__init__,konekcija,"nesto",'127.0.0.1')
    
if __name__=="__main__":
    unittest.main()