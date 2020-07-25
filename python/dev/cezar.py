'''
alphabet -a b c d e f g h ...
code - d e f g h i j k ...
key: 3

text - baca
code - edfd
'''

import unittest
import string


# add to different file
def cezar(text: str, key: int) -> str:
    alphabet = string.ascii_lowercase
    code = alphabet[key:] + alphabet[:key]
    table = str.maketrans(alphabet, code)
    return text.translate(table)


class TestCezar(unittest.TestCase):

    def test_coding(self):
        self.assertEqual(cezar("baca", 3), 'edfd')

    def test_uncoding(self):
        self.assertEqual(cezar("edfd", -3), "baca")
