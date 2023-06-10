import unittest
from translator import english_to_french, french_to_english

class TestEtoF(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Morning"),"Matin") # test when "Hello" is given as input the output is "Bonjour".

class TestFtoE(unittest.TestCase): 
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello") # test when "Bonjour" is given as input the output is "Hello".


unittest.main()