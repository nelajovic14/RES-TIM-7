import unittest
from ObradaPoruke import obrada

class TestObradaPoruke(unittest.TestCase):
    def test_obrada(self):
        ulazna_poruka = "Server primio podatke od korisnika: Nebitni Nebitnic\nid: 1\npotrošnja: 2\nmesec: januar"
        povratna_poruka = "1, 2, januar"
        self.assertEqual(obrada(ulazna_poruka), povratna_poruka)
    def test_exception(self):
        poruka=",,nestp"
        self.assertRaises(IndexError,obrada,poruka)

if __name__ == "__main__":
    unittest.main()