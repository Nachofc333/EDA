# IGNACIO FERNÁNDEZ CAÑEDO



"""
Created on Thu Apr 28 18:20:30 2022
"""
import random
from bst import BinarySearchTree
from bintree import BinaryTree

class MyBST(BinarySearchTree):
    
    def get_odd_siblings(self):
        list = []
        return self._get_odd_siblings(self._root, list)

    def _get_odd_siblings(self, node, list):
        if node is not None:
            self._get_odd_siblings(node.right, list)
            i = len(list)
            if node.left:
                if node.left.elem % 2 != 0:
                    if node.right:
                        list.append(node.right.elem)
            if node.right:
                if node.right.elem % 2 != 0:
                    if node.left:
                        list.append(node.left.elem)
            self._get_odd_siblings(node.left, list)

        """                            # En mi solución todos los elementos que deben ser incluidos en la lista son incluidos
        j = 1                          # pero no en el orden que indica el unittest, cambian 1 o 2 numeros de sitio.
        for i in range(len(list)):     # Con este cacho de código comentado si salen todos los unittest, pero como dice
            if j < len(list):          # en el enunciado, no se puede ordenar la lista usando otros métodos, por ello lo
                if list[i] < list[j]:  # dejo aqui comentado y no lo incluyo en la solución.
                    elem1 = list[j]
                    elem2= list[i]
                    list[i] = elem1
                    list[j] = elem2
            j += 1"""
        return list
