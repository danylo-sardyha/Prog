import unittest
from Lab1 import zigzag 

class TestZigzagTraverse(unittest.TestCase):
    
    def test_m5_n5(self):
        matrix = [
            [ 1,  2,  3,  4,  5],
            [ 6,  7,  8,  9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        expected = [
            1, 2, 6, 11, 7, 3, 4, 8, 12, 16, 21, 17, 13, 9, 5, 
            10, 14, 18, 22, 23, 19, 15, 20, 24, 25
        ]
        self.assertEqual(zigzag(matrix), expected)
        
    def test_m2_n4(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]
        expected = [1, 2, 5, 6, 3, 4, 7, 8]
        self.assertEqual(zigzag(matrix), expected)

    def test_m6_n1(self):
        matrix = [
            [1], [2], [3], [4], [5], [6]
        ]
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(zigzag(matrix), expected)

    def test_m1_n1(self):
        matrix = [
            [42]
        ]
        expected = [42]
        self.assertEqual(zigzag(matrix), expected)
    
    def test_m3_m3(self):
        matrix=[
            [1], [2], [3],
            [4], [5], [6],
            [7], [8], [9]    
              ]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(zigzag(matrix), expected)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)