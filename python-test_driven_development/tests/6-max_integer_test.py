#!/usr/bin/python3
"""Unittests for max_integer function."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_list_with_neg_and_pos(self):
        self.assertEqual(max_integer([-1, 0, 100, -50]), 100)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 2, 3]), 9)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 7, 3]), 7)

    def test_strings(self):
        self.assertEqual(max_integer(["a", "z", "c"]), "z")

    def test_string_argument(self):
        self.assertEqual(max_integer("holberton"), "t")

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])


if __name__ == '__main__':
    unittest.main()
