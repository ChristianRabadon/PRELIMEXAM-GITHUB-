import unittest
from unittest.case import TestCase

def Fahrenheit(a,b,c,d):

    return (a-b)*(c/d)

class TestConversion(unittest.TestCase):
    
    def test (self):
        self.assertEqual(((32-32)*(5/9)),0)

if __name__ == '__main__':
    unittest.main()