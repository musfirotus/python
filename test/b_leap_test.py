import unittest
import sys
sys.path.append('./src/')
from b_leap import LeapYear
class TestLeap(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(LeapYear(2020), "Kabisat")
        
    def test_not_equal(self):
        self.assertNotEqual(LeapYear(2020), "Kabisat.")
        
    def test_not_int(self):
        self.assertRaises(ValueError, LeapYear, '3')

if __name__ == '__main__':
    unittest.main()