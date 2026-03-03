import unittest
from Lab2 import max_hamsters

class TestHamsters(unittest.TestCase):

    def test_example_1(self):
        S = 7
        C = 3
        hamsters = [[1, 2], [2, 2], [3, 1]]
        self.assertEqual(max_hamsters(S, C, hamsters), 2)

    def test_example_2(self):
        S = 19
        C = 4
        hamsters = [[5, 0], [2, 2], [1, 4], [5, 1]]
        self.assertEqual(max_hamsters(S, C, hamsters), 3)

    def test_example_3(self):
        S = 2
        C = 2
        hamsters = [[1, 5], [1, 6]]
        self.assertEqual(max_hamsters(S, C, hamsters), 1)

    def test_example_4(self):
        S = 32
        C = 2
        hamsters = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(max_hamsters(S, C, hamsters), 2)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
