# Test Script: python -m unittest super_reduced_string_tes.py

# Super Reduced String
# https://www.hackerrank.com/challenges/reduced-string/problem

import unittest
from super_reduced_string import superReducedString


class TestSuperReducedString(unittest.TestCase):

    def test_superReducedString1(self):
        self.assertEqual("abd",
                         superReducedString("aaabccddd"))

    def test_superReducedString2(self):
        self.assertEqual("Empty String",
                         superReducedString("aa"))

    def test_superReducedString3(self):
        self.assertEqual("Empty String",
                         superReducedString("abba"))


if __name__ == '__main__':
    unittest.main()
