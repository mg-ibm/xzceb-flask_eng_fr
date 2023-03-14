import unittest

from translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase):

    def test_french_to_english_translations_match(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test_french_to_english_input_not_null(self):
        self.assertNotEqual(french_to_english("Bonjour"), None)
        


class TestEnglishToFrench(unittest.TestCase):

    def test_english_to_french_translations_match(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_english_to_french_input_not_null(self):
        self.assertNotEqual(english_to_french("Hello"), None)
        

unittest.main()
