import unittest
import sys
sys.path.append('./src/')
from c_rate import Rate
class TestRate(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(Rate(4), "SEMUA USIA")
        
    def test_not_equal(self):
        self.assertNotEqual(Rate(21), "DEWASA.")
        
    def test_not_int(self):
        self.assertRaises(ValueError, Rate, '-3')

if __name__ == '__main__':
    unittest.main()