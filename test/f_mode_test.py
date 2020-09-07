import unittest
import sys
sys.path.append('./src/')

from f_mode import Mode

class charsTest(unittest.TestCase):
        
    def test_equal(self):
        self.assertEqual(Mode([1,2,3,4,5,6,6,8,6]), 4)
        
    def test_not_equal(self):
        self.assertNotEqual(Mode('saya'), 5)
        
    def test_not_angka(self):
        self.assertRaises(ValueError, Mode, 3)

if __name__ == '__main__':
    unittest.main()