# -*- coding: utf-8 -*-
"""SList.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D0ngznuRvN9LDbiiittrqoWhv8WTBMZr
"""

import random


class SNode:

    def __init__(self, e):
        self.elem = e
        self.next = None


class SList:

    def __init__(self):
        self._head = None
        self._size = 0

    def isEmpty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def __str__(self):
        x = '['
        current = self._head
        while current:
            x += str(current.elem) + ','
            current = current.next
        x = x[:-1] + ']'
        return x

    def addFirst(self, e):

        node = SNode(e)
        node.next = self._head
        self._head = node
        self._size += 1

    def removeFirst(self):
        if self.isEmpty():
            print('Empty list')
            return

        e = self._head.elem
        self._head = self._head.next
        self._size -= 1
        return e

    def addLast(self, e):
        node = SNode(e)
        current = self._head
        if self.isEmpty():
            self._head = node
        else:
            while current.next:
                current = current.next
            current.next = node
        self._size += 1

    def removeOdd(self):
        if self.isEmpty():
            print("lista vacia")
            return
        while self._head.elem % 2 != 0 and not self.isEmpty():
            self._head = self._head.next
            self._size -= 1
        current = self._head
        while current.next:
            if current.next.elem % 2 != 0:
                current.next = current.next.next
                self._size -= 1
            else:
                current = current.next




    def insertAt(self, e, index):
        if index > self.size:
            print('índice fuera de rango')
            return
        node = SNode(e)
        current = self._head
        for i in range(index - 1):
            current = current.next
        node.next = current.next
        current.next = node


L = SList()

for i in range(8, 0, -1):
    L.addFirst(random.randint(0, 9))
print(L, L._size)

for i in range(3):
    L.removeFirst()
print(L, L._size)

for i in range(3):
    L.addLast(random.randint(10, 19))
print(L, L._size)

L.removeOdd()
print(L, L._size)