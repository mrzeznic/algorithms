***
alfabet - a b c d e f g h ...
kod - d e f g h i j k ...
klucz: 3

tekst - baca
szyfr - edfd
***

import unittest
import string


#add to different file
def cezar(napis: str, klucz: int) -> str:
    alfabet.string.ascii_lowercase
    kod = alfabet[klucz:] + alfabet[:klucz]
    tabela = str.maketrans(alfabet,kod)
    return napis.translate(tabela)



class TestCezar(unittest.TestCase):

    def test_kodowania (self):
        self.assertEqual(cezar("baca", 3),'edfd')
        
    def test_odkodowania(self):
        self.assertEqual(cezar("edfd",-3),"baca")