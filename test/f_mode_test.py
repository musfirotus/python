import unittest
import sys
sys.path.append('./src/')

from f_mode import Mode

class ModeTest(unittest.TestCase):
        
    def test_equal(self):
        self.assertEqual(Mode([1,2,3,4,5,6,6,8,6]), 6)
        
    def test_not_equal(self):
        self.assertNotEqual(Mode([1,2,3,4,5,6,6,8,6]), 5)
        
    def test_not_angka(self):
        self.assertRaises(ValueError, Mode, {1,2,3,4,5,6,6,8,6})

if __name__ == '__main__':
    unittest.main()