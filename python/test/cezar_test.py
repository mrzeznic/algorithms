import unittest
from cezar import cezar


class TestCezar(unittest.TestCase):

    def test_coding(self):
        self.assertEqual(cezar("baca", 3), 'edfd')

    def test_uncoding(self):
        self.assertEqual(cezar("edfd", -3), "baca")
