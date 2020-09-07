import unittest
import sys
sys.path.append('./src/')

from a_char import Chars

class charsTest(unittest.TestCase):
        
    def test_equal(self):
        self.assertEqual(Chars('saya'), 4)
        
    def test_not_equal(self):
        self.assertNotEqual(Chars('saya'), 5)
        
    def test_not_angka(self):
        self.assertRaises(ValueError, Chars, 3)

if __name__ == '__main__':
    unittest.main()