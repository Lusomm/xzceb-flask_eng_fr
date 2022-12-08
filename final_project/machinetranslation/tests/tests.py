""" Hallo """
import unittest

from translator import english_2_french, french_2_english

class TestTranslator(unittest.TestCase):
    """ Tschau """
    def test1_e2f(self):
        """ fasd """
        self.assertEqual(english_2_french(None), None)

    def test2_e2f(self):
        """ fasd """
        self.assertEqual(english_2_french("Hello"), "Bonjour")

    def test3_e2f(self):
        """ fasd """
        self.assertEqual(english_2_french(""), None)
    
    def test1_f2e(self):
        """ fasd """
        self.assertEqual(french_2_english(None), None)
    
    def test2_f2e(self):
        self.assertEqual(french_2_english("Bonjour"), "Hello")

    def test3_f2e(self):
        self.assertEqual(french_2_english(""), None)

unittest.main()
