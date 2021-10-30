import unittest
import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append('..'))
from translator import english_to_french, french_to_english
class TestenglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        #self.assertEqual(english_to_french('Lady'), 'Dame')
        
    def test2(self):
        self.assertEqual(english_to_french(None), '')
class TestfrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        #self.assertEqual(french_to_english('Dame'), 'Lady')
        
    def test2(self):
        self.assertEqual(french_to_english(None), '')
unittest.main()