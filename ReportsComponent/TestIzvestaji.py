import unittest
from Izvestaji import *

class TesteIzvestaji(unittest.TestCase):
    def test_ulica(self):
        vrednost = (("Tolstojeva", "Mart", 1500), ("Tolstojeva", "April", 3000))
        self.assertEqual(IzvestajUlica("Tolstojeva"), vrednost)
    def test_brojilo(self):
        vrednost = ((1, "Mart", 1500), (1, "April", 3000))
        self.assertEqual(IzvestajBrojilo(1), vrednost)

if __name__ == "__main__":
    unittest.main()
  