import random


class DNode:
    def __init__(self, elem):
        self.elem = elem
        self.prev = None
        self.next = None


class Dlist():
    def __init__(self):
        """Creates an empty list"""
        self._head = None
        self._tail = None
        self._size = 0

    def isEmpty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def __str__(self):
        text = "["
        current = self._head
        while current:
            text += str(current.elem) + ","
            current = current.next
        text = text[:-1]
        text += "]"
        return text

    def addFirst(self, elem):
        node = DNode(elem)
        if not self.isEmpty():
            self._head.prev = node
        else:
            self._tail = node
        node.next = self._head
        self._head = node
        self._size += 1

    def removeLast(self):
        if self.isEmpty():
            return "Lista vacia"
        else:
            e_tail = self._tail.elem
            self._tail = self._tail.prev
            if self._size > 1:
                self._tail.next = None
            elif self._size == 1:
                self._head = None
            self._size -= 1
        return e_tail

    def insertAt(self, elem, pos):
        node = DNode(elem)
        # llegar al objeto previo al indice donde quiero insertarlo
        if pos > self._size:
            print("index out of range")
            return
        current = self._head
        if pos == 0 or self.isEmpty():
            self.addFirst(elem)
        elif pos == len(self):
            self.addLast(elem)

        else:
            for i in range(pos-1):
                current = current.next

            node.next = current.next
            node.prev = current
            current.next.prev = node
            current.next = node
            self._size += 1







    def addLast(self, elem):
        node = DNode(elem)
        if not self.isEmpty():
            self._head.prev = node
        else:
            self._head = node
        node.next = self._tail
        self._tail = node
        self._size += 1

    def removeAt(self, pos, elem):
        pass

def IdentificarPal(palabra):
    D = Dlist()
    for i in palabra:
        D.addLast(i)
    current1 = D._head
    current2 = D._tail
    for i in range(len(D)//2):
        if current1.elem != current2.elem:
            return False
        current1 = current1.next
        current2 = current2.prev
    return True


DL = Dlist()

print(IdentificarPal("reconocer"))
print(DL)
