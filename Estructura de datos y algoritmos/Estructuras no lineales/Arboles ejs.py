from bintree import BinaryTree
from bst import BinarySearchTree
import random


class BST2(BinarySearchTree):
    #ej 1
    def minimum(self):
        if self._root is None:
            return
        return self._minimum(self._root)
    def _minimum(self, node):
        if node.left is None:
            return node.elem
        return self._minimum(node.left)
    #ej2
    def maximum(self):
        if self._root is None:
            return
        return self._maximum(self._root)

    def _maximum(self, node):
        if node.right is None:
            return node.elem
        return self._maximum(node.right)
    #ej 3
    def sum_todos(self):
        if self._root is None:
            return
        return self._sum_todos(self._root)

    def _sum_todos(self, node):
        if node is None:
            return 0
        return node.elem + self._sum_todos(node.left) + self._sum_todos(node.right)
    #ej 4
    def prints10(self):
        if self._root.left is None and self._root.right is None or self._root is None:
            return
        return self._prints10(self._root, None, None)

    def _prints10(self, node, parent, grand):
        if node is None:
            return
        if grand and grand.elem%10==0:
            print(node.elem)
        self._prints10(node.left, node, parent)
        self._prints10(node.right, node, parent)


T = BST2()
for i in range(12):
    T.insert(random.randint(0, 20))

T.draw()
print(T.minimum())
print(T.sum_todos())
print(T.prints10())
