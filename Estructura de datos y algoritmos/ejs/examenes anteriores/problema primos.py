class Node:
    def __init__(self, elem, left=None, right=None, parent=None):
        self.elem = elem
        self.left = left
        self.right = right
        self.parent = parent


class MyBST:

    def __init__(self):
        self.root = None

    def depth(self, node):
        if node == None or node.parent == None:
            return 0

        return 1 + self.depth(node.parent)

    def find(self, x):
        """Returns True if x exists into the True, eoc False"""
        return self._find(self.root, x)

    def _find(self, node, x):
        """Returns the node whose elem is x.
        If this does not exist, it returns None"""
        if node == None:
            return None
        if node.elem == x:
            return node
        if x < node.elem:
            return self._find(node.left, x)
        if x > node.elem:
            return self._find(node.right, x)

    def insert(self, x):
        """inserts a new node, with element x, into the tree"""
        if self.root == None:
            self.root = Node(x)
        else:
            self._insertNode(self.root, x)

    def _insertNode(self, node, x):
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

    def getPaG(self, a):
        return self._getPag(self.root, a, None, None)

    def _getPag(self, node, a, parent, grandpa):
        if node is None:
            return node
        if node.elem == a:
            return grandpa
        elif a < node.elem:
            return self._getPag(node.left, a, node, parent)
        elif a > node.elem:
            return self._getPag(node.right, a, node, parent)

    def checkCousins(self, x, y):
        node1 = self.find(x)
        print(node1)
        node2 = self.find(y)
        print(node2)
        if node1 is None or node2 is None:
            return False

        grandpa1 = self.getPaG(node1.elem)
        grandpa2 = self.getPaG(node2.elem)

        if grandpa1 == grandpa2:
            if grandpa1.left.left == node1 and grandpa2.left.right == node2:
                return False
            elif grandpa1.right.right == node1 and grandpa2.right.left == node2:
                return False
            return True
        else:
            return False

"""returns True if x and y are cousins, and False eoc"""
"""nodeX = self.find(x)
        nodeY = self.find(y)
        if nodeX == None or nodeY == None:
            return False

        depthX = self.depth(nodeX)
        depthY = self.depth(nodeY)

        if depthX != depthY:
            return False

        if nodeX.parent == nodeY.parent:
            return False

        if nodeX.parent.parent != nodeY.parent.parent:
            return False

        return True"""

import unittest


class Test(unittest.TestCase):
    # provisional mark
    mark = 0

    def setUp(self):
        values = [12, 16, 19, 20, 4, 14, 2, 18, 10, 8, 24, 6, 1, 13]
        self.bst = MyBST()
        for x in values:
            self.bst.insert(x)

        self.data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

        self.bst.draw()

    def test7_printNota(self):
        print('\n\n*************************')
        print("\t Provisional mark:", Test.mark)
        print('*************************')

    def test1_checkCousins(self):
        print('Caso 1: a does not in the tree, a=', self.data[0], ', b=', self.data[1])
        self.assertEqual(self.bst.checkCousins(self.data[0], self.data[1]), False)
        print('\t\t mark += 1')
        Test.mark += 1

    def test2_checkCousins(self):
        print('Caso 2: b does not in the tree, a=', self.data[1], ', b=', self.data[5])
        self.assertEqual(self.bst.checkCousins(self.data[0], self.data[1]), False)
        print('\t\t mark += 1')
        Test.mark += 1

    def test3_checkCousins(self):
        print('Caso 3: a y b have different depths, a=', self.data[1], ', b=', self.data[4])
        self.assertEqual(self.bst.checkCousins(self.data[1], self.data[4]), False)
        print('\t\t mark += 3')
        Test.mark += 3

    def test4_checkCousins(self):
        print('Caso 4: a and b are siblings, a=', self.data[2], ', b=', self.data[10])
        self.assertEqual(self.bst.checkCousins(self.data[2], self.data[10]), False)
        print('\t\t mark += 5')
        Test.mark += 5

    def test5_checkCousins(self):
        print('Caso 5: a and b are not cousing and not siblings, a=', self.data[8], ', b=', self.data[13])
        self.assertEqual(self.bst.checkCousins(self.data[8], self.data[13]), False)
        print('\t\t mark += 5')
        Test.mark += 5

    def test6_checkCousins(self):
        print('Caso 6: a and b are  cousins a=', self.data[2], ', b=', self.data[19])
        self.assertEqual(self.bst.checkCousins(self.data[2], self.data[19]), True)
        print('\t\t mark += 5')
        Test.mark += 5

    # Comentar para usarlo en google colab
unittest.main(argv=['first-arg-is-ignored'], exit=False)

    # Descomenar para usarlo en Spyder
    # if __name__ == '__main__':
    #    unittest.main()