# from binarysearchtree import BinarySearchTree
from bst import BinarySearchTree
from bst import BinaryNode


class AVLTree(BinarySearchTree):

    # Override insert method from base class to keep it as AVL
    def insert(self, elem: object) -> None:
        """inserts a new node, with key and element elem"""
        self._root = self._insert(self._root, elem)

    def _insert(self, node: BinaryNode, elem: object) -> BinaryNode:
        """gets a node, searches the place to insert a new node with element e (using super()._insert),  and then,
        the function has to balance the node returned by the function super.()_insert"""
        node = super()._insert(node, elem)
        node = self._rebalance(node)
        return node

    # Override remove method from base class to keep it as AVL
    def remove(self, elem: object) -> None:
        self._root = self._remove(self._root, elem)

    def _remove(self, node: BinaryNode, elem: object) -> BinaryNode:
        """ gets a node, searches the node with element elem in the subtree that hangs down node , and
        then remove this node (using super()._remove). After this, the function has to balance the node returned by the function super()._remove"""
        node = super()._remove(node, elem)
        node = self._rebalance(node)
        return node

    def _is_balanced(self, node):
        altura_nodo = self._height(node)
        hr = 0
        hl = 0
        if node.right:
            hr = self._height(node.right)
            hr += 1
        if node.left:
            hl = self._height(node.left)
            hl += 1
        resta = abs(hr - hl)
        return resta <= 1

    def _rebalance(self, node: BinaryNode) -> BinaryNode:
        """ gets node and balances it"""
        if node is None:
            return node
        if not self._is_balanced(node):
            print(node)
            if node.left and not node.right:
                if node.left.left:
                    if self._height(node.left.left) >= self._height(node.left.right):
                        print("Simple rara R")
                        node = self.rotate_right(node)
                else:
                    node = self.double_left_right(node)
            elif node.right and not node.left:
                if node.right.right:
                    if self._height(node.right.right) >= self._height(node.right.left):
                        print("Simple rara L")
                        node = self.rotate_left(node)
                else:
                    node = self.double_right_left(node)
            elif node.left and node.right:
                if self._height(node.right) > self._height(node.left):
                    node = self.rotate_left(node)
                elif self._height(node.right) < self._height(node.left):
                    node = self.rotate_right(node)
        return node

    def getPaG(self, a):
        return self._getPag(self._root, a, None, None)

    def _getPag(self, node, a, parent, grandpa):
        if node is None:
            return node
        if node.elem == a:
            return parent
        elif a < node.elem:
            return self._getPag(node.left, a, node, parent)
        elif a > node.elem:
            return self._getPag(node.right, a, node, parent)

    def rotate_right(self, node):
        print("Rotate Right")
        self.draw()
        parent = self.getPaG(node.elem)
        if not node.left.right:
            if node == self._root:
                node.left.right = BinaryNode(node.elem)
                return node.left
            elif parent.right == node:
                parent = self.getPaG(node.elem)
                parent.right = node.left
                parent.right.right = BinaryNode(node.elem)
                return parent.right
            elif parent.left == node:
                parent = self.getPaG(node.elem)
                parent.left = node.left
                parent.left.right = BinaryNode(node.elem)
                return parent.left
        else:
            if node == self._root:
                hijo1 = node.left.right
                hijo2 = node.left
                node.left.right = node
                node.left = hijo1
                return hijo2
            else:
                parent = self.getPaG(node.elem)
                parent.left = node.left
                node.left = parent.left.right
                parent.left.right = node
                return parent.left

    def rotate_left(self, node):
        print("Rotate Left", node)
        self.draw()
        parent = self.getPaG(node.elem)
        if not node.right.left:
            if node == self._root:
                node.right.left = BinaryNode(node.elem)
                return node.right
            elif parent.left == node:
                parent.left = node.right
                parent.left.left = BinaryNode(node.elem)
                return parent.left
            elif parent.right == node:
                parent = self.getPaG(node.elem)
                nodo = node
                parent.right = node.right
                parent.right.left = BinaryNode(nodo.elem)
                return parent.right
        else:
            if node == self._root:
                hijo1 = node.right.left
                hijo2 = node.right
                node.right.left = node
                node.right = hijo1
                return hijo2
            else:
                parent = self.getPaG(node.elem)
                parent.right = node.right
                node.right = parent.right.left
                parent.right.left = node
                return parent.right

    def double_right_left(self, node):
        print("r")
        self.draw()
        hijo = node.right
        node.right = node.right.left
        node.right.right = BinaryNode(hijo.elem)
        self.draw()
        return self.rotate_left(node)

    def double_left_right(self, node):
        print("l")
        self.draw()
        hijo = node.left
        node.left = node.left.right
        node.left.left = BinaryNode(hijo.elem)
        self.draw()
        return self.rotate_right(node)

    def getNonLeaves(self):
        return self._getNonLeaves(self._root)

    def _getNonLeaves(self, node):
        lista = []
        if node.left or node.right:
            lista.append(node.elem)

        return lista


if __name__ == '__main__':

    """tree2 = AVLTree()
    data = [5, 6, 4, 3, 7, 8]
    for e in data:
        tree2.insert(e)
    tree2.draw()"""

    """data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for e in data:
        tree3.insert(e)
        tree3.draw()"""


    tree = AVLTree()
    data = [17, 8, 12, 2, 7, 27, 48, 58, 3, 4]
    for n in data:
        tree.insert(n)
    tree.draw()

    """"# newNode = BinaryNode(2)
    # left = BinaryNode(3, newNode, None)
    #left = BinaryNode(3, None, None)
    #right = None
    # right = BinaryNode(9)

    # right.left = BinaryNode(8)
    # right.right = BinaryNode(20)
    # rrNode = right.right
    # rrNode.right = BinaryNode(30)

    #root = BinaryNode(5, left, right)

    #tree._root = root"""
"""data = [4, 3, 2, 5, 7, 6, 8, 9]
    for e in data:
        tree.insert(e)"""


