#!/usr/bin/python3
"""Unittest for max_integer(list)
"""
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """Test case for max_integer function."""

    def test_max_in_positive_integers(self):
        """Test with a list of positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_in_negative_integers(self):
        """Test with a list of negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_in_mixed_integers(self):
        """Test with a list of mixed integers."""
        self.assertEqual(max_integer([-1, 2, 0, 3]), 3)

    def test_max_in_floats(self):
        """Test with a list of floats."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_max_in_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_max_in_single_element_list(self):
        """Test with a list containing a single element."""
        self.assertEqual(max_integer([42]), 42)

    def test_max_in_identical_elements(self):
        """Test with a list containing identical elements."""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

if __name__ == '__main__':
    unittest.main()

