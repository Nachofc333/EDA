# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 12:00:17 2022

@author: SECRETARIA
"""

from bintree import BinaryTree
from bst import BinarySearchTree


class MyBST(BinarySearchTree):
    
    def get_diam(self):
        x = 0
        return self._get_diam(self._root, x)

    def _get_diam(self, node, x):
        if node == None:
            return x
        if not node.left and not node.right:
            return 1
        if node.right:
            x1 = max(self._height(node.right.left), self._height(node.right.right)) + 1
            x += x1 + 1 if x < x1 + 1 else x
        if node.left:
            x2 = max(self._height(node.left.right), self._height(node.left.left)) + 1
            x += x2 + 1 if x < x2 + 1 else x
        return x + 1

