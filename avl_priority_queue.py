class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 1

class AVLPriorityQueue:
    def __init__(self):
        self.root = None

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _right_rotate(self, y):
        x = y.left
        mid_subtree = x.right

        x.right = y
        y.left = mid_subtree

        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        return x

    def _left_rotate(self, x):
        y = x.right
        mid_subtree = y.left

        y.left = x
        x.right = mid_subtree

        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def insert(self, value, priority):
        self.root = self._insert_recursive(self.root, value, priority)

    def _insert_recursive(self, root, value, priority):
        if not root:
            return Node(value, priority)

        if priority >= root.priority:
            root.left = self._insert_recursive(root.left, value, priority)
        else:
            root.right = self._insert_recursive(root.right, value, priority)

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        
        balance = self._get_balance(root)

        """LL""" 
        if balance > 1 and priority >= root.left.priority:
            return self._right_rotate(root)
        
        """LR"""
        if balance > 1 and priority < root.left.priority:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)

        """RR"""
        if balance < -1 and priority < root.right.priority:
            return self._left_rotate(root)

        """RL"""
        if balance < -1 and priority >= root.right.priority:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    def pop(self):
        if not self.root:
            raise IndexError("Спроба видалення з порожньої черги")
        
        self.root, popped_node = self._pop_max(self.root)
        return popped_node.value, popped_node.priority

    def _pop_max(self, root):
        if not root.left:
            return root.right, root
        
        root.left, popped_node = self._pop_max(root.left)

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        balance = self._get_balance(root)

        if balance > 1:
            if self._get_balance(root.left) >= 0:
                return self._right_rotate(root)
            else:
                root.left = self._left_rotate(root.left)
                return self._right_rotate(root)

        if balance < -1:
            if self._get_balance(root.right) <= 0:
                return self._left_rotate(root)
            else:
                root.right = self._right_rotate(root.right)
                return self._left_rotate(root)

        return root, popped_node

    def peek(self):
        if not self.root:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.value, current.priority

    def view_all(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, root, result):
        if root:
            self._inorder_traversal(root.left, result)
            result.append((root.value, root.priority))
            self._inorder_traversal(root.right, result)