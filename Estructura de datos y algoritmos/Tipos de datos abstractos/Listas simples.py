"""
SNode clase de nodo de listas enlazadas con los atributos:
 el atributo lo llamamos elem
 el otro atributo es el objeto siguiente en la lista y se llama next
hay que poner los atributos al crear el constructor

SList es la clase de la lista enlazada con los atributos:
 head, el nodo en primera posicion
 y size el numero de elementos de la lista
"""


class SNode:
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class Slist:
    def __init__(self):
        self._head = None
        self._size = 0

    def isEmpty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def __str__(self):
        text = "["
        current = self._head
        while current != None:
            text += str(current.elem) + ","
            current = current.next
        text = text[:-1] + "]"
        return text

    def addFirst(self, elem):
        node = SNode(elem)
        node.next = self._head
        self._head = node
        self._size += 1

    def removeFirst(self):
        if self.isEmpty():
            print("Error")
            e = "Lista vacia"
        else:
            e = self._head.elem
            self._head = self._head.next
            self._size -= 1
        return e

    def removeLast(self):
        current = self._head
        if self.isEmpty():
            print("Lista vacia")
            return "Lista vacia"
        else:
            while current.next:
                current = current.next
                e = current
                e = self._head.next
                self._size -= 1
            return e

    def addLast(self, elem):
        node = SNode(elem)
        current = self._head
        if self.isEmpty():
            self._head = node
        else:
            while current.next:
                current = current.next
            current.next = node
        self._size += 1

    def getAt(self, pos):
        if self.isEmpty():
            return "Lista vacia"
        else:
            current = self._head
            if current.elem == self.Index(pos):
                return current.elem
            else:
                current = current.next
    def Index(self, pos):
        if self.isEmpty():
            return "Lista vacia"
        else:
            current = self._head
            cont = 0
            if pos == cont:
                return current.elem
            cont = 1
            while current.next:
                if pos == cont:
                    return current.next.elem
                current = current.next
                cont += 1



    def insertAt(self, elem, index):
        if index > self._size:
            print("indice fuera de rango")
            
        else:
            node = SNode(elem)
            current = self._head
            for i in range(index-1):
                current = current.next
            node.next = current.next
            current.next = node

    def removeAt(self, pos):
        if self.isEmpty():
            print("Lista vacia")
            return "Lista vacia"
        else:
            current = self._head
            while current.next:
                if current.next.elem == pos:
                    current.next = current.next.next

                    self._size -= 1
                else:
                    current = current.next



L = Slist()
for i in range(8, 0, -1):
    L.addFirst(i)
print(L)
for i in range(3):
    L.removeFirst()
print(L)
print(L._size)

for i in range(15, 18):
    L.addLast(i)
print(L)
L.removeAt(5)
print(L)
print(L.Index(4))
L.getAt(3)
print(L)