import csv
import unittest
from lab6Sort import *

class Testing(unittest.TestCase):
    def test_BubbleSort(self):
        
        footballers = [ ["Rivaldo", 8, "Brazil"],
        ["Jürgen Klinsmann", 11, "Germany"],
        ["Pelé", 12, "Brazil"],
        ["Gary Lineker", 10, "England"],
        ["Miroslav Klose", 16, "Germany"],
        ["Just Fontaine", 13, "France"],
        ["Thomas Müller", 10, "Germany"]]

        #self.assertEqual(sorted(footballers, key=lambda x: x[1], reverse=True), BubbleSort(footballers))
        footballers_test = footballers.copy()
        BubbleSort(footballers_test)
        self.assertListEqual(sorted(footballers, key=lambda x: x[1], reverse=True), footballers_test)
    
    def test_returnTopFive(self):
        
        footballers = [ ["Rivaldo", 8, "Brazil"],
        ["Jürgen Klinsmann", 11, "Germany"],
        ["Pelé", 12, "Brazil"],
        ["Gary Lineker", 10, "England"],
        ["Miroslav Klose", 16, "Germany"],
        ["Just Fontaine", 13, "France"],
        ["Thomas Müller", 10, "Germany"]]

        sorted_footballer = sorted(footballers, key=lambda x: x[1], reverse=True)
        self.assertListEqual(sorted_footballer[:5], returnTopFive(sorted_footballer))

if __name__ == '__main__':
    unittest.main()