import unittest

from Lab9 import search_finite_automata

class TestFASearch(unittest.TestCase):

    def test_standard(self):
        self.assertEqual(search_finite_automata("hello world", "world"), [6])

    def test_multiple_occurrences(self):
        self.assertEqual(search_finite_automata("АБРАКАДАБРА", "АБРА"), [0, 7])

    def test_overlapping(self):
        self.assertEqual(search_finite_automata("aaaaa", "aa"), [0, 1, 2, 3])
        self.assertEqual(search_finite_automata("abababa", "aba"), [0, 2, 4])

    def test_not_found(self):
        self.assertEqual(search_finite_automata("abcdef", "xyz"), [])

    def test_empty_cases(self):
        self.assertEqual(search_finite_automata("", "abc"), [])
        self.assertEqual(search_finite_automata("abc", ""), [])

    def test_longer_needle(self):
        self.assertEqual(search_finite_automata("hi", "hello"), [])

    def test_cyrillic_and_special(self):
        self.assertEqual(search_finite_automata("тест! тест?", "тест"), [0, 6])

if __name__ == '__main__':
    unittest.main()