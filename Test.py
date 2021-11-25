#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from Prog1 import summation

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        data = [23, 32]
        result = get_abs_diff(data)
        self.assertEqual(result, 9)

if __name__ == '__main__':
    unittest.main()
