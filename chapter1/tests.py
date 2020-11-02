from unittest import TestCase
from chapter1.arrays_and_strings import *


class IsUniqueTestCase(TestCase):
    def test_unique_string(self):
        string = "abcdefghijklmnopqrstuvwxzy"
        self.assertTrue(is_unique(string))

    def test_non_unique_string(self):
        string = "abcdefgg"
        self.assertFalse(is_unique(string))


class CheckPermutationTestCase(TestCase):
    def test_is_permutation(self):
        string_1 = "abcd"
        string_2 = "dcba"
        self.assertTrue(check_permutation(string_1, string_2))
        self.assertTrue(check_permutation(string_2, string_1))

    def test_is_not_permutation(self):
        string_1 = "abcd"
        string_2 = "xabc"
        self.assertFalse(check_permutation(string_1, string_2))
        self.assertFalse(check_permutation(string_2, string_1))

    def test_is_not_permutation_diff_lengths(self):
        string_1 = "abc"
        string_2 = "abcd"
        self.assertFalse(check_permutation(string_1, string_2))
        self.assertFalse(check_permutation(string_2, string_1))


class URLifyTestCase(TestCase):
    def test_urlify(self):
        # example given in book
        input = "Mr John Smith     "
        length = 13
        self.assertEqual("Mr%20John%20Smith", urlify(input, length))


class PalindromePermutationTestCase(TestCase):
    def test_palindrome_permutation(self):
        # example in book
        str = "Tact Coa"
        self.assertTrue(palindrome_permutation(str))

    def test_non_palindrome_permutation(self):
        str = "Tact Coat"
        self.assertFalse(palindrome_permutation(str))
        str_2 = "aabbddccxs"
        self.assertFalse(palindrome_permutation(str_2))


class OneAwayTestCase(TestCase):
    # Using Examples in Book
    def test_one_away(self):
        self.assertTrue(one_away("pale", "ple"))
        self.assertTrue(one_away("pales", "pale"))
        self.assertTrue(one_away("pale", "bale"))

    def test_more_than_one_away(self):
        self.assertFalse(one_away("pale", "bake"))


class StringCompressionTestCase(TestCase):
    def test_string_compression_shorter(self):
        str = "aabcccccaaa"
        self.assertEqual("a2b1c5a3", string_compression(str))

    def test_string_compression_longer(self):
        str = "aabcde"
        self.assertEqual(str, string_compression(str))


# class RotateMatrixTestCase(TestCase):

