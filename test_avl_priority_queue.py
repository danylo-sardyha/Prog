import unittest
import math
from avl_priority_queue import AVLPriorityQueue

class TestAVLPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.pq = AVLPriorityQueue()

    def test_insert_and_peek(self):
        self.pq.insert("A", 10)
        self.assertEqual(self.pq.peek(), ("A", 10))
        
        self.pq.insert("B", 20)
        self.assertEqual(self.pq.peek(), ("B", 20))
        
        self.pq.insert("C", 5)
        self.assertEqual(self.pq.peek(), ("B", 20))

    def test_pop_order(self):
        elements = [("A", 10), ("B", 50), ("C", 5), ("D", 20), ("E", 100)]
        for val, prio in elements:
            self.pq.insert(val, prio)

        expected_order = [("E", 100), ("B", 50), ("D", 20), ("A", 10), ("C", 5)]
        
        for expected_val, expected_prio in expected_order:
            self.assertEqual(self.pq.pop(), (expected_val, expected_prio))

    def test_equal_priorities(self):
        self.pq.insert("Task 1", 10)
        self.pq.insert("Task 2", 10)
        self.pq.insert("Task 3", 10)

        # Перевіряємо, що елементи з однаковим пріоритетом витягуються коректно
        results = [self.pq.pop() for _ in range(3)]
        for val, prio in results:
            self.assertEqual(prio, 10)
            self.assertIn(val, ["Task 1", "Task 2", "Task 3"])

    def test_empty_pop_raises_error(self):
        with self.assertRaises(IndexError):
            self.pq.pop()

    def test_view_all(self):
        self.pq.insert("Low", 1)
        self.pq.insert("High", 100)
        self.pq.insert("Medium", 50)
        
        expected = [("High", 100), ("Medium", 50), ("Low", 1)]
        self.assertEqual(self.pq.view_all(), expected)

    def test_avl_balancing_height(self):
        n = 1000
        for i in range(1, n + 1):
            self.pq.insert(f"Item {i}", i)

        # Висота AVL-дерева має бути <= 1.44 * log2(n + 2) - 0.328
        max_allowed_height = 1.44 * math.log2(n + 2)
        actual_height = self.pq.root.height
        
        self.assertLessEqual(actual_height, max_allowed_height, 
                             "Дерево не збалансоване як AVL-дерево!")

if __name__ == '__main__':
    unittest.main()