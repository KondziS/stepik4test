import unittest
from main import sum_two_numbers

class TestStringMethods(unittest.TestCase):

    def test_sum_two_numbers(self):
        self.assertEqual(sum_two_numbers(2, 4), 6)

if __name__ == '__main__':
    unittest.main()