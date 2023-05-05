import os, sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour") # test when "Hello" translates to "Bonjour"
        self.assertNotEqual(english_to_french("Hello"), None)
        self.assertEqual(english_to_french("Computer"), "Ordinateur") # test when "Hello" translates to "Bonjour"
        self.assertEqual(english_to_french("I want some food"), "Je veux de la nourriture")  # test when "I want some food" translates to "Je veux de la nourriture"
        self.assertEqual(english_to_french(), "")  # test when empty translates to ""
        self.assertEqual(english_to_french(''), "")  # test when empty string translates to ""
        self.assertEqual(english_to_french(None), "")  # test when empty string translates to ""
        
class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english("Bonjour le monde"), "Hello World") # test when "Bonjour le monde" translates to "Hello World"
        self.assertEqual(french_to_english("Programme"), "Program") # test when "Programme" translates to "Program"
        self.assertNotEqual(french_to_english("Programme"), None)
        self.assertEqual(french_to_english(), "")  # test when empty translates to ""
        self.assertEqual(french_to_english(''), "")  # test when empty string translates to ""
        self.assertEqual(french_to_english(None), "")  # test when empty string translates to ""

unittest.main()
