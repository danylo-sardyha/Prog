import unittest
from Lab3 import BinaryTree, find_successor

class TestBinaryTreeSuccessor(unittest.TestCase):
    def setUp(self):
        #         10
        #        /  \
        #       5    15
        #      / \     \
        #     3   7     20
        #              /
        #            12
        
        self.root = BinaryTree(10)
        self.node5 = BinaryTree(5, parent=self.root)
        self.node15 = BinaryTree(15, parent=self.root)
        self.root.left = self.node5
        self.root.right = self.node15
        self.node3 = BinaryTree(3, parent=self.node5)
        self.node7 = BinaryTree(7, parent=self.node5)
        self.node5.left = self.node3
        self.node5.right = self.node7
        self.node20 = BinaryTree(20, parent=self.node15)
        self.node15.right = self.node20
        self.node12 = BinaryTree(12, parent=self.node20)
        self.node20.left = self.node12

    def test_of_7_to_10(self):
        successor = find_successor(self.root, self.node7)
        self.assertEqual(successor.value, 10)

    def test_of_15_to_12(self):
        successor = find_successor(self.root, self.node15)
        self.assertEqual(successor.value, 12)

    def test_of_3_to_5(self):
        successor = find_successor(self.root, self.node3)
        self.assertEqual(successor.value, 5)

    def test_20_last(self):
        successor = find_successor(self.root, self.node20)
        self.assertIsNone(successor)

if __name__ == "__main__":
    unittest.main()