from contextlib import nullcontext
import unittest
from unittest import mock
from WriterTerminal import *
from WriterClass import Message
from unittest.mock import Mock

class TestWriterTerminal(unittest.TestCase):
    def test_logovanje(self):
        self.assertNotEqual(logovanje,True,True)
    def test_unos_podataka(self):
        self.assertRaises(TypeError,unos_podataka, nullcontext)
    def test_konekcija(self):
        self.assertRaises(socket.error,konekcija)
        
if __name__ == "__main__":
    unittest.main(verbosity=2, exit = False)