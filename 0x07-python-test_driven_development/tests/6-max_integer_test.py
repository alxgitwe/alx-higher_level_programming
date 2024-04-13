#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests  max_integer function"""
    def setUp(self):
        self.ordered_list_2 = [10, 20, 30, 40]
        self.unordered_list_2 = [10, 30, 40, 20]

    def test_max_values_2(self):
        self.assertEqual(max_integer(self.ordered_list_2),
                         max_integer(self.unordered_list_2))

    def test_string_2(self):
        self.assertEqual(max_integer("another_string"), 't')

    def test_nothing_2(self):
        self.assertEqual(max_integer(), None)

    def test_empty_list_2(self):
        self.assertEqual(max_integer([]), None)

    def test_list_of_negatives_2(self):
        self.assertEqual(max_integer([-2, -99, -54]), -2)

    def test_key_error_2(self):
        with self.assertRaises(KeyError):
            max_integer({10 : 6})

    def test_type_error_too_many_args_2(self):
        with self.assertRaises(TypeError):
            max_integer('list', 'of_tuples')

    def test_type_error_on_incomparable_list_items_2(self):
        with self.assertRaises(TypeError):
            max_integer([{}, []])
