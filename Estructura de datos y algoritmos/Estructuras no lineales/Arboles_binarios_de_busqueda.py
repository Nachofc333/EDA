"""
un arbol binario de busqueda es un arbol ordenado con complejidad logaritmica
equilibrar:
    Para ordenar un arbol binario de hijos, cada nodo tiene que tener 1 de altura mas o la misma en sus dos hijos
    rotacion simnple derecha:
        Si un nodo tiene solo 1 hijo a su izquierda y ese hijo tiene solo otro hijo a la izquierda, el hijo del medio pasa a ser el padre y tendra
        dos hijos, el que antes era su padre y su hijo(rotacion simple derecha)
        Si el hijo del medio tiene un hijo derecho tambien, este pasara a ser el hijo izquierdo del padre
    doble rotacion simple derecha:
        El segundo nodo tiene un hijo derecho, ese hijo pasa a ser el primer hijo y se hace una rotacion simple derecha


"""


class BinaryNode:
    """This implementation only saves the references to the children"""

    def __init__(self, elem: object,
                 left: "BinaryNode" = None,
                 right: "BinaryNode" = None) -> None:
        self.elem = elem
        self.left = left
        self.right = right

    def __eq__(self, other: 'BinaryNode') -> bool:
        """checks if two nodes (subtrees) are equal o not"""
        return other is not None and self.elem == other.elem and \
               self.left == other.left and self.right == other.right


class BinaryTree:
    def __init__(self) -> None:
        """creates an empty binary tree
        I only has an attribute: _root"""
        self._root = None

    def __eq__(self, other: 'BinaryTree') -> bool:
        """checks if two binary trees are equal o not"""
        return other is not None and self._root == other._root

    def size(self) -> int:
        """Returns the number of nodes"""
        return self._size(self._root)

    def _size(self, node: 'BinaryNode') -> int:
        """return the size of the subtree from node"""
        if node is None:
            return 0
        else:
            return 1 + self._size(node.left) + self._size(node.right)

    def height(self) -> int:
        """Returns the height of the tree"""
        return self._height(self._root)

    def _height(self, node: 'BinaryNode') -> int:
        """return the height of node"""
        if node is None:
            return -1

        return 1 + max(self._height(node.left), self._height(node.right))

    def preorder(self) -> None:
        """prints the preorder (root, left, right) traversal of the tree"""
        self._preorder(self._root)

    def _preorder(self, node: 'BinaryNode') -> None:
        """prints the preorder (root, left, right) traversal of the subtree
        than hangs from node"""
        if node is not None:
            print(node.elem)
            self._preorder(node.left)
            self._preorder(node.right)

    def postorder(self) -> None:
        """prints the postorder (left, right, root)  traversal of the tree"""
        self._postorder(self._root)

    def _postorder(self, node: 'BinaryNode') -> None:
        """prints the postorder (left, right, root) traversal of the subtree
        than hangs from node"""
        if node is not None:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.elem)

    def inorder(self) -> None:
        """prints the inorder (left, root, right)  traversal of the tree"""
        self._inorder(self._root)

    def _inorder(self, node: 'BinaryNode') -> None:
        """prints the inorder (left, root, right) traversal of the subtree
        than hangs from node"""
        if node is not None:
            self._inorder(node.left)
            print(node.elem)
            self._inorder(node.right)

    def level_order(self) -> None:
        """prints the level order of the tree.
        We will use an array (Python List) to save the
        nodes that you are visiting. Instead of using an array,
        you could use a Queue (import queue)"""
        if self._root is None:
            print('tree is empty')
        else:
            # we use a Python list to save the binary nodes
            q = [self._root]
            while not q.empty():
                current = q.pop(0)  # dequeue, get the first node
                print(current.elem)
                if current.left is not None:
                    q.append(current.left)
                if current.right is not None:
                    q.append(current.right)

    def draw(self) -> None:
        """function to draw a tree. """
        if self._root:
            self._draw('', self._root, False)
        else:
            print('tree is empty')
        print('\n\n')

    def _draw(self, prefix: str, node: 'BinaryNode',is_left: bool) -> None:
        if node is not None:
            self._draw(prefix + "     ", node.right, False)
            print(prefix + "|-- " + str(node.elem))
            self._draw(prefix + "     ", node.left, True)

    def search(self, elem:object):
        """Returns the node whose elem is elem"""
        return self._search(self._root, elem)

    def _search(self, node: BinaryNode, elem: object):
        ''' Recursive function '''
        if node is None or node.elem == elem:
            return node
        elif elem < node.elem:
            return self._search(node.left, elem)
        elif elem > node.elem:
            return self._search(node.right, elem)


    def insert(self, elem: object):
        """inserts a new node which elem is elem. The root must be replaced with the new subtree after inserting elem
        in the subtree that hangs down the root"""
        self._root = self._insert(self._root, elem)

    def _insert(self, node:BinaryNode, elem:object):
        """recursive function that takes a node and an elem.
        it recursively searches its right location and then inserts it.
        The function returns the new subtree updated with the new node"""
        if node is None:
            return BinaryNode(elem)
        if node.elem == elem:
            print("Error, elem ya existe")
            return node
        if elem < node.elem:
            node.left = self._insert(node.left, elem)
        else:  # elem > node.elem
            node.right = self._insert(node.right, elem)
        return node

    def remove(self, elem:object):
        """update the root with the new subtree after remove elem"""
        self._root = self._remove(self._root, elem)

    def _remove(self, node:BinaryNode, elem: object):
        """removes from the subtree node, the node whose element is elem.
        returns the subtree node updated after removing elem"""
        if node is None:
            print(elem, "Not found")
            return node
        if elem < node.elem:
            node.left = self._remove(node.left, elem)
        elif elem > node.elem:
            node.right = self._remove(node.right, elem)
        else:  # elem == node.elem
            if node.left is None and node.right is None:
                #Case 1: node no tiene hijos
                return None
            # Case 2: Tiene un hijo
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Case 3: Tiene 2 hijos
            successor = self._minimum_node(node.right)
            node.elem = successor.elem
            node.right = self._remove(node.right, successor.elem)
        return node


    def _minimum_node(self, node: BinaryNode):
        """returns the node with the smallest elem in the subtree node.
        this is the node that is furthest to the left"""
        min_node = node
        while min_node.left is not None:
            min_node = min_node.left
        return min_node

