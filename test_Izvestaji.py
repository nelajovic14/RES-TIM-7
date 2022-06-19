import unittest
from unittest import mock
from unittest import result
from unittest.mock import MagicMock, Mock,patch
from Izvestaji import izvestaj_brojilo,izvestaj_ulica,Baza,connection_string,funkcija_za_izvestaje,OpenFile
import cx_Oracle
class TestIzvestaji(unittest.TestCase):
    def test_ulica(self):
        self.assertRaises(TypeError, izvestaj_ulica, int(1))
    def test_brojilo(self):
        self.assertRaises(TypeError, izvestaj_brojilo, "string")
        
    def test_ulica_ime(self):
        self.assertEqual(True,izvestaj_ulica("Tolstoj"))
        
    def test_brojilo_ime(self):
        self.assertEqual(True,izvestaj_brojilo("1"))
    
    def test_query(self):
        baza=Baza(connection_string)
        query="select b.idb, p.mesec, sum(p.potrosnjaa) as potrosnja from brojilo b, POTROSNJAKOR p where b.idb = p.brojiloid and b.idb=2 group by b.idb,  p.mesec"
        self.assertRaises(cx_Oracle.DatabaseError,baza.do_query,query)
        
    def test_query_with_result(self):
        baza=Baza(connection_string)
        query="select b.idb, p.mesec, sum(p.potrosnjaa) as potrosnja from brojilo b, POTROSNJAKO p where b.idb = p.brojiloid and b.idb=2 group by b.idb,  p.mesec"
        self.assertRaises(cx_Oracle.DatabaseError,baza.do_query_with_result,query)
        
    def test_execute(self):
        query="select b.idb, p.mesec, sum(p.potrosnjaa) as potrosnja from brojilo b, POTROSNJAKOR p where b.idb = p.brojiloid and b.idb=2 group by b.idb,  p.mesec"
        mock_baza=Mock()
        Baza.do_query_with_result(mock_baza,query)
        mock_baza.connection.cursor().execute.assert_called_with(query)
    def test_execute2(self):
        query="INSERT INTO POTROSNJA VALUES (555,1,50,\'novembar\')"
        mock_baza=Mock()
        Baza.do_query(mock_baza,query)
        mock_baza.connection.cursor().execute.assert_called_with(query)
  
    @patch('builtins.input')
    def test_funkciju_za_izvestaje(self,input_value):
        input_value.side_effect=["exit"]
        mock_print=mock.Mock(side_effect=lambda:(print("Ukoliko zelite izvestaj za ulicu unesite 1, a za brojilo unesite 2, za izlazak exit: ")))
        self.assertEqual(mock_print(),funkcija_za_izvestaje())
        
    def test_file(self):
        f=OpenFile()
        self.assertIsInstance(f,OpenFile)

    def test_file_read(self):
        mock_file=Mock()
        OpenFile.read_from_file(mock_file)
        mock_file.fajl.read.assert_called()
        mock_file.fajl.close()

    def test_file_write(self):
        mock_file=Mock()
        OpenFile.write_in_file(mock_file,"something")
        mock_file.fajl.write.assert_called()
        mock_file.fajl.close()

    def test_fajl(self):
        odg = "korisnicci.txt"
        mock_fajl=Mock()
        response = OpenFile.open_with_mode(mock_fajl,odg,"r")
        ocekivanje = -1
        self.assertEqual(ocekivanje, response)
        mock_fajl.fajl.close()

if __name__ == "__main__":
    unittest.main()
  