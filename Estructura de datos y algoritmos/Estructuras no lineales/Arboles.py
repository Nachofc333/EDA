"""
-----------------------------
CONCEPTOS BASICOS

Raiz: el unico nodo que no tiene padre(A)
Nodo interno: Nodo que al menos tiene un hijo(A,B,C,F)
Nodo hoja: Nodo sin hijos
Hermanos: nodos con el mismo padre
Ascendientes y descendientes
Subarbol: arbol formado por un nodo y todos sus descendientes
----------------------------
el tamaño de un arbol viene dado por el numero de sus nodos
si un arbol tiene n nodos, tendra n-1 aristas
la profundidad de un nodo es la longitud de dicho nodo a la raiz
la raiz tiene profundidad 0
la altura de un nodo es la longitud a una hoja
La altura de un arbol vacio es -1
Camino: camino entre X e Y que permita alcanzarse a traves de descendientes
el grado de un nodo es el numero de hijos directos
Durante el curso vamos a ver Arboles binarios, de grado 2
un arbol binario puede tener grado 0,1 o 2
------------------------------
recorrido Pre-order: primero se visita la raiz, despues el arbol izq y finalmente el subarbol drch(root, left, right)
recorrido Post-order: primero se visita el subarbol izq, despues el subarbol drch y finalmente la raiz(left, right, root)
recorrido In-order: Primero visitamos el subarbol izq, despues la raiz y finalmente el subarbol drch(left, root, right)


"""
class Node():
    def __init__(self, elem, left=None, right=None, parent=None):
        self._elem = elem
        self._parent = parent
        self._left = left
        self._right = right

class BTree():
    def __init__(self, root=None):
        self._root = root

    def size(self):
        if self._root == None:
            return 0
        return self._size(self._root)

    def _size(self, node):
        if not node:
            return 0
        return 1 + self._size(node._left)+self._size(node._right)

    def height(self):
        if self._root == None:
            return -1
        return self._height(self._root)

    def _height(self, node):
        if not node:
            return 0
        elif node == self._root and not self._root._right and not self._root._left:
            return 0
        return 1 + max(self._height(node._left), self._height(node._right))


N1, N2, N3, N4, N5, N6 = Node(5), Node(7), Node(2), Node(9), Node(8), Node(6)

N6 = Node(6, None, None, N4)
N4 = Node(9, N6, None, N3)
N5 = Node(8, None, None, N3)
N3 = Node(2, N5, N4, N1)
N2 = Node(7, None, None, N1)
N1 = Node(5, N3, N2, None)

B = BTree(N1)

print(B.size())
print(B.height())




