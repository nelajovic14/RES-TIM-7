import unittest
from unittest import mock
from Reader import konekcija,provera_id,upis_u_bazu
from KonekcijaKaBazi import Baza
from konekcija import Konekcija
from unittest.mock import Mock,patch


class TestReader(unittest.TestCase):   
    def test_input_values_proverId(self):
        self.assertRaises(TypeError,provera_id,"hello",True)
        self.assertRaises(TypeError,provera_id,True,"hello")
    def test_input_values_upisUBazu(self):
        self.assertRaises(TypeError,upis_u_bazu,True)
        self.assertRaises(TypeError,upis_u_bazu,True,False)
        self.assertRaises(TypeError,upis_u_bazu,False,False,0)
    def test_konekcija(self):
        self.assertAlmostEqual(konekcija(),True)
    
class TestWithMock(unittest.TestCase):
    def test_base_connection(self):      
        mock=Mock(Baza('bp1/ftn@localhost'))
        mock.__call__()
    def test_connection(self):
        mock=Mock(Konekcija(10003,"127.0.0.1"))
        mock.__call__()


if __name__=="__main__":
    unittest.main()