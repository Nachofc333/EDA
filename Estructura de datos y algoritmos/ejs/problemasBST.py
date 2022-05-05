# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 13:58:23 2022

"""
from bst import BinarySearchTree
from bintree import BinaryTree, BinaryNode


class BST2(BinarySearchTree):
    def minimum(self) -> object:
        """returns the smallest key of the tree. What is its temporal complexity?"""
        # Complexity: O(log n)
        if self._root is None:
            print('tree is empty')
            return None

        node = self._root
        while node.left:
            node = node.left

        return node.elem

    def minimum_rec(self) -> object:
        """recursive function to return the smallest elem"""
        return self._minimum_rec(self._root)

    def _minimum_rec(self, node: 'BSTNode') -> object:
        if node is None:
            return None  # base case
        elif node.left is None:
            return node.elem  # base case
        else:
            return self._minimum_rec(node.left)  # recursive case

    def maximum(self) -> object:
        """returns the greatest elem of the tree. What is its temporal complexity?"""
        # Complexity: O(log n)
        if self._root is None:
            print('tree is empty')
            return None

        node = self._root
        while node.right:
            node = node.right

        return node.elem

    def maximum_rec(self) -> object:
        """recursive function that returns the largest object"""
        return self._maximum_rec(self._root)

    def _maximum_rec(self, node: 'BSTNode') -> object:
        if node is None:
            return None  # base case
        elif node.right is None:
            return node.elem  # base case
        else:
            return self._maximum_rec(node.right)  # base recursive

    def sum_elems(self) -> object:
        """ returns the sum of all its elems. What is its temporal complexity?"""
        # Complexity: O(n), where n is the size of the tree.
        # The function has to visit all the nodes of the tree.
        return self._sum_elems(self._root)

    def _sum_elems(self, node: 'BSTNode') -> object:
        if node:
            return node.elem + self._sum_elems(node.left) + self._sum_elems(node.right)
        else:
            return 0

    def prints10(self) -> None:
        """prints the elems of those nodes whose grandparents' elems are multiply of 10
        What is its temporal complexity"""
        # Complexity: O(n), where n is the size of the tree.
        # The function has to visit all the nodes of the tree.
        self._prints10(self._root, None, None)

    def _prints10(self, node: 'BSTNode', parent: 'BSTNode', grand: 'BSTNode') -> None:
        if node:
            self._prints10(node.left, node, parent)
            if grand and grand.elem % 10 == 0:
                print(node.elem, end=' ')
            self._prints10(node.right, node, parent)

    def _maximum_node(self, node: 'BSTNode') -> 'BSTNode':
        """returns the node with the maximum elem in the subtree node.
        This is the node that is furthest to the right
        """
        max_node = node
        while max_node.right is not None:
            max_node = max_node.right
        return max_node

    def _remove(self, node: 'BSTNode', elem: object) -> 'BSTNode':
        if node is None:
            return None

        if elem < node.elem:
            node.left = self._remove(node.left, elem)
        elif elem > node.elem:
            node.right = self._remove(node.right, elem)
        else:
            # elem == node.elem
            if node.left is None and node.right is None:
                # node is a leave
                node = None
            elif node.left is None:  # only has the right child
                return node.right
            elif node.right is None:  # only has the left child
                return node.left
            else:  # elem == node.elem
                predecessor = self._maximum_node(node.left)
                print('predecessor: ', predecessor.elem)
                node.elem = predecessor.elem
                node.left = self._remove(node.left, predecessor.elem)

        return node

    def fe_size(self, elem: object) -> int:
        """gives an elem, and returns the size balance factor of
        its node """
        node = self.search(elem)
        return self._fe_size(node)

    def _fe_size(self, node: 'BSTNode') -> int:
        """returns the size balance factor of the input node"""
        if node is None:
            return 0
        else:
            return abs(self._size(node.left) - self._size(node.right))

    def is_size_balanced(self) -> bool:
        """return True if the tree is size balanced"""
        return self._is_size_balanced(self._root)

    def _is_size_balanced(self, node: 'BSTNode') -> bool:
        """returns True if the node is size balanced;
        a node is balanced if its size factor is <=1 and
        its two children are size balanced"""
        if node:
            return self._fe_size(node) <= 1 and \
                   self._is_size_balanced(node.left) and \
                   self._is_size_balanced(node.right)
        else:
            return True

    def fe_height(self, elem: object) -> int:
        """gives an elem, and returns the height balance factor of
        its node """
        node = self.search(elem)
        return self._fe_height(node)

    def _fe_height(self, node: 'BSTNode') -> int:
        """returns the height balance factor of the input node"""
        if node is None:
            return 0
        else:
            return abs(self._height(node.left) - self._height(node.right))

    def is_height_balanced(self) -> bool:
        """return True if the tree is height balance, that is,
        if its root is height balanced"""
        return self._is_height_balanced(self._root)

    def _is_height_balanced(self, node: 'BSTNode') -> bool:
        """return True if the node is balanced, False e.o.c
        A node is balanced if its height balance <=1 and
        its two children are height balanced"""
        if node:
            return self._fe_height(node) <= 1 and \
                   self._is_height_balanced(node.left) and \
                   self._is_height_balanced(node.right)
        else:
            return True

# 2º parcial
class Node:
    def __init__(self,elem,left=None,right=None,parent=None):
        self.elem=elem
        self.left=left
        self.right=right
        self.parent=parent

class MyBST():
    def __init__(self):
        self.root = None

    def insert(self, x):
        """inserts a new node, with element x, into the tree"""
        if self.root == None:
            self.root = Node(x)
        else:
            self._insertNode(self.root, x)

    def _insertNode(self, node, x):
        """método recursivo"""
        if node.elem == x:
            # print('Error: la clave ya existe. No permitimos duplicados')
            return

        if x < node.elem:

            if node.left == None:
                # ya he encontrado su sitio
                newNode = Node(x)
                newNode.parent = node
                node.left = newNode
            else:
                self._insertNode(node.left, x)

        else:  # x>node.elem

            if node.right == None:
                # ya he encontrado la posición
                newNode = Node(x)
                newNode.parent = node
                node.right = newNode
            else:
                self._insertNode(node.right, x)

    def draw(self):
        """Function to draw the tree"""
        self._draw('', self.root, False)
        print()

    def _draw(self, prefix, node, isLeft):
        if node != None:
            self._draw(prefix + "     ", node.right, False)
            print(prefix + ("|-- ") + str(node.elem))
            self._draw(prefix + "     ", node.left, True)

    def getListNonLeaves(self):
        """returns a list with the keys of the nodes that are not leaves"""
        result = []
        self._getListNonLeaves(self.root, result)
        return result

    def _getListNonLeaves(self, node, lst_nonleaves):
        if node != None:
            if node.left:
                self._getListNonLeaves(node.left, lst_nonleaves)
            if node.left != None or node.right != None:
                lst_nonleaves.append(node.elem)
            self._getListNonLeaves(node.right, lst_nonleaves)


values = [25, 20, 36, 10, 22, 30, 40, 5, 12, 28, 38, 48]
tree = MyBST()
for x in values:
    tree.insert(x)
tree.draw()
print('getNonLeaves()', tree.getListNonLeaves())


"""if __name__ == "__main__":
    tree = BST2()
    for x in [50, 60, 30, 20, 24, 70, 66, 65, 10, 80, 21, 15, 35, 45, 22]:
        tree.insert(x)

    print('input tree:')
    tree.draw()
    print()
    print('Minimum elem of the tree:', tree.minimum())
    print('Maximum elem of the tree:', tree.maximum())
    print('sum of all its elems:', tree.sum_elems())
    print("elems whose grandparents' elems are multiply of 10")
    tree.prints10()
    print()

    tree.remove(50)
    # 50 should have been replaced by 45 as root
    print('after remove 50')
    tree.draw()

    tree.remove(70)
    print('after remove 70')
    # 70 should have been replaced by 66 as root
    tree.draw()

    tree.remove(20)
    # 20 should have been replaced by 15 as root
    print('after remove 20')
    tree.draw()

    tree.insert(55)
    tree.insert(36)
    tree.insert(50)
    tree.insert(32)
    tree.insert(56)
    print('after insert 55,36,50,32,56')
    tree.draw()
    print()
    for x in [45, 60, 30, 15, 35, 10, 24, 21, 66, 80, 63, 55, 36, 50, 32, 56]:
        print('size-balanced factor of  {} is {}'.format(x, tree.fe_size(x)))
        print('height-balanced factor of  {} is {}'.format(x, tree.fe_height(x)))
        print()"""""