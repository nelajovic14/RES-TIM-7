import unittest
from unittest import mock
from WriterTerminal import *
from unittest.mock import Mock

class TestWriter(unittest.TestCase):
    def test_logovanje(self):
        #self.assertRaises(FileNotFoundError,Logovanje)
        self.assertNotEqual(Logovanje,True,True)
    def test_unos(self):
        self.assertRaises(TypeError,UnosPodataka,nullcontext)
    def test_konekcija(self):
        self.assertRaises(socket.error,konekcija)
        
if __name__=="__main__":
    unittest.main()