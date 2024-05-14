# test_math_operations.py
import unittest
from homepage import add_two_numbers

class TestMathOperations(unittest.TestCase):

    def test_add_two_numbers(self):
        result = add_two_numbers(3, 5)
        self.assertEqual(result, 8, "Expected sum of 3 + 5 to be 8")

    def test_add_two_numbers_negative(self):
        result = add_two_numbers(-3, 5)
        self.assertEqual(result, 2, "Expected sum of -3 + 5 to be 2")

    def test_add_two_numbers_zero(self):
        result = add_two_numbers(0, 0)
        self.assertEqual(result, 0, "Expected sum of 0 + 0 to be 0")

if __name__ == '__main__':
    unittest.main()