#!/usr/bin/python3
"""max_integer unittests"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTest(unittest.TestCase):
    """Define unittest for max_integer[]"""

    def ordered_list_test(self):
        """Test an ordered list of integers."""
        ordered_list = [1, 3, 7, 9]
        self.assertEqual(max_integer(ordered_list), 9)

    def unordered_list_test(self):
        """Test an unordered list of integers."""
        unordered = [7, 1, 9, 3]
        self.assertEqual(max_integer(ordered_list), 9)

    def empty_list(self):
        """Test an empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def max_at_the_beginning(self):
        """Test a list of max integer at the beggining"""
        mx = [4, 3, 2, 1]
        self.assertEqual(max_integer(mx), 4)

    def test_floats(self):
        """Test max integer of floats"""
        flt = [2.33, 4.55, 1.22, -9.42, 0.13]
        self.assertEqual(max_integer(flt), 4.55)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 16]
        self.assertEqual(max_integer(ints_and_floats), 16)

    def test_string(self):
        """Test a string."""
        string = "Nenes"
        self.assertEqual(max_integer(string), 's')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Mimi", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [12]
        self.assertEqual(max_integer(one_element), 12)

if __name__ == '__main__':
    unittest.main()
