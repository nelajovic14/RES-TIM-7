import unittest
from unittest import mock
from Reader import *
from unittest.mock import Mock,patch


class TestReader(unittest.TestCase):   
    def test_input_values_proverId(self):
        self.assertRaises(TypeError,provera_id,"hello")
        self.assertRaises(TypeError,provera_id,True)
        self.assertRaises(TypeError,provera_id,"nesto")
    def test_input_values_upisUBazu(self):
        self.assertRaises(TypeError,upis_u_bazu,True)
        self.assertRaises(TypeError,upis_u_bazu,True,False)
        self.assertRaises(TypeError,upis_u_bazu,False,False,0)
    def test_konekcij(self):
        self.assertAlmostEqual(konekcija(),True)
    
class TestWithMock(unittest.TestCase):
    def test_base_connection(self):
        #Baza.__init__(real,'bp1/ftn@localhost')
        #real.doQuery=Mock()
        #query=str("INSERT INTO POTROSNJA VALUES ("+str(5)+","+str(5)+","+str(500)+",\'jun\')")
        #real.doQuery.assert_called_once_with(query)
        #real.doQuery()
        mock=Mock(Baza('bp1/ftn@localhost'))
        mock.__call__()
        #con = cx_Oracle.connect('bp1/ftn@localhost')
        #mock.return_value=con
      
        #mock.assert_called_once_with()
        #thing = nullcontext
        #Baza.__init__(thing,'bp1/ftn@localhost')
        #thing.doQuery = Mock(return_value=con)
        #mock.doQuery.assert_call(query)
        


if __name__=="__main__":
    unittest.main()