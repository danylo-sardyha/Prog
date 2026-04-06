class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self._value = value
        self._left = left
        self._right = right
        self._parent = parent

    def get_value(self):
        return self._value

    def get_left(self):
        return self._left

    def get_right(self):
        return self._right

    def get_parent(self):
        return self._parent

    def set_left(self, node):
        self._left = node
        if node is not None:
            node._parent = self

    def set_right(self, node):
        self._right = node
        if node is not None:
            node._parent = self
    def find_successor(self):
        if self.get_right() is not None:
            current = self.get_right()
            while current.get_left() is not None:
                current = current.get_left()
            return current

        current = self
        while current.get_parent() is not None and current.get_parent().get_right() == current:
            current = current.get_parent()

        return current.get_parent()