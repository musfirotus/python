import unittest
import sys
sys.path.append('./src/')
from d_trim import Trim
class TestTrim(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(Trim("ini adalah tulisan yang sangat panjang",1), "ini")
        
    def test_not_equal(self):
        self.assertNotEqual(Trim("ini adalah tulisan yang sangat panjang",1), "ini.")
        
    def test_not_int(self):
        self.assertRaises(ValueError, Trim, "ini adalah tulisan yang sangat panjang", '1')

if __name__ == '__main__':
    unittest.main()