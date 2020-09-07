import unittest
import sys
sys.path.append('./src/')
import a_char

class TestCharacter(unittest.TestCase):
    def is_equal(self):
        self.assertEqual(a_char.Chars('saya'), 4)
        
    def is_not_equal(self):
        self.assertNotEqual(a_char.Chars('saya'), 2)
        
    def is_not_integer(self):
        self.assertRaises(ValueError, a_char.Chars, 3)

if __name__ == '__main__':
    unittest.main()