import unittest
import sys
sys.path.append('./src/')
from e_convert import Convert
class TestConvert(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(Convert(4), "Empat")
        
    def test_not_equal(self):
        self.assertNotEqual(Convert(4), "Empat.")
        
    def test_not_int(self):
        self.assertRaises(ValueError, Convert, '3')

if __name__ == '__main__':
    unittest.main()