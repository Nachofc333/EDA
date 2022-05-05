import unittest
from slist import SList, SNode
import sys

class SList2(SList):

    def __init__(self):
        super().__init__() # llama al constructor de la superclase
        """This constructor creates an empty list"""
        self._head=None
        self._size=0

    def sumLastN(self, n):
        result = 0
        #if n < 0:
        #    result = None
        #else:
         #   if n > self._size:
          #      n = self._size
           # interval = range(self._size - n, self._size)  # intervalo en el que actua la funcion
            #for item in interval:
             #   num = self.getAt(item)
              #  result += num
        #return result
        if n < 0: #si la lista está vacía devuelve None
            result = None

        else:
            if n > self._size: #si n es mayor que la longitud de la lista sumará todos los elemente de la lista
                n = self._size #por lo que n será igual a la longitud total de la lista

            current = self._head #nos permitirá recorrer la lista
            for i in range(self._size -n): #recorremos la lista hasta la posición correcta dependiendo del valor de n
                current = current.next

            for i in range(n): #sumamos los últimos n elementos
                result += current.elem
                current = current.next
        return result

    # method for inserting a new node in the middle
    def insertMiddle(self, elem):
        current = self._head
        newNode = SNode(elem)
        if self._size == 0:  # si la lista está vacía se añade directamente al principio de la lista
            self.addFirst(elem)
            return
        elif self._size % 2 == 0:  # si la longitud de la lista es par insertaremos el elemento en la posición len(self)//2
            for i in range(len(self) // 2 - 1):  # llegamos a la posición len(self)//2. Como nuestra variable current ya está en la primera posición de la lista
                current = current.next  # hay que realizar el bucle len(self)//2 -1 veces para llegar justo al medio. Sino nos pasaríamos de la mitad de la lista
        else:  # si la longitud de la lista es par insertaremos el elemento en la posición len(self +1)//2
            for i in range((len(self) + 1) // 2 - 1):  # llegamos a la posición len(self +1)//2. Como nuestra variable current ya está en la primera posición de la lista
                current = current.next  # hay que realizar el bucle len(self +1)//2 -1 veces para llegar justo al medio. Sino nos pasaríamos de la mitad de la lista
        newNode.next = current.next  # Una vez que hemos llegado a la posición deseada,
        current.next = newNode  # introducimos el nuevo nodo enlazándolo con el resto de la lista

    """def insertList(self, inputList, start, end):
        if start < 0 or start > end or end >= len(self):
            print("Error, start debe ser mayor que cero y menor que end y end debe ser menor que len")
            return
        newcurrent = inputList._head

        if start == 0:
            for i in range(end + 1):
                self._head = self._head.next

            for i in range(len(inputList)):
                e = newcurrent.elem
                self.addFirst(e)
                self._size += 1
        else:
            current = self._head

            for i in range(start - 1):
                current = current.next

            for i in range(end - start + 1):
                current.next = current.next.next
                self._size -= 1

            for i in range(len(inputList)):
                e = newcurrent.elem
                newNode = SNode(e)
                newNode.next = current.next
                current.next = newNode
                current = newNode
                newcurrent = newcurrent.next
                self._size += 1"""

    """def insertList(self, inputList, start, end):
        if start < 0 or start > end or end >= len(self):
            print("Error, start debe ser mayor que cero y menor que end y end debe ser menor que len")
            return
        current = self._head

        for i in range(start - 1):
            current = current.next

        for i in range(start - end + 1):
            current.next = current.next.next
            self._size -= 1

        newcurrent = inputList._head

        for i in range(len(inputList)):
            e = newcurrent.elem
            newNode = SNode(e)
            newNode.next = current.next
            current.next = newNode
            current = newNode
            newNode = newNode.next
            self._size += 1"""

    def insertList(self, inputList, start, end):
        if start < 0 or start > end or end >= len(self):  # requisitos por los que la función debe hacer return
            print("Error, start debe ser mayor que cero y menor que end y end debe ser menor que len")
            return
        newcurrent = inputList._head  # variable que recorrerá la lista a introducir
        current = self._head # variable que recorrerá la lista
        if start > 0:
            for i in range(start - 1):  # bucle para que el current llegue hasta el elemento en la posicion start
                current = current.next

        for i in range(end) if start == 0 else range(end-start +1):  # este bucle borrará los elementos que hay hasta la posición end
            current.next = current.next.next
            self._size -= 1

        for i in range(len(inputList)):  # bucle que introduce los elementos de la inputlist en la slista
            e = newcurrent.elem
            newNode = SNode(e)  # se crea el nodo con el elemento que queremos introducir
            newNode.next = current.next
            current.next = newNode  # introducimos el nuevo nodo enlazándolo con el resto de la lista
            current = current.next
            newcurrent = newcurrent.next
            self._size += 1
        if start == 0:
            self._head = self._head.next  # actualizar la cabeza y borra al primer elemento
            self._size -= 1




    """def reverseK(self, k):   # tarda mas
        if k <= 1:  # si k es 1 o menos devuelve la lista igual
            print("k tiene que ser mayor que 1")
            return SList2
        if k > len(self):  # si k es mayor que la longitud de la lista, iguala k al size para invertir toda la lista
            k = self._size
        current = self._head
        current2 = self._head
        listaux = SList()  # esta es una lista auxiliar para introducir los elementos cambiados
        auxcurrent = None  # el current que recorrera la lista auxiliar
        while current:
            for i in range(k):  # bucle para el primer current
                listaux.addFirst(current.elem)  # introduce en la lista aux el elemento del primer current
                current = current.next
            auxcurrent = listaux._head  # asigna la cabeza al current de la lista auxiliar
            for i in range(k):  # bucle para el segundo current que ira asignando los valores ya cambiados
                current2.elem = auxcurrent.elem  # se asignan los valores de la lista auxiliar que ya esta cambiada
                current2 = current2.next
                auxcurrent = auxcurrent.next
            if k > self._size/2:  # este if solo sirve para cuando k vale mas que la lista / 2
                k = self._size - k  # esto hace que la k una vez llegue a lo maximo, lo vuelva a hacer pero con la llista restante para no pasarse de indice
                                    # por ejemplo si la lista tiene len 6 y pones k = 4, invertira los 4 primeros y despues hace k = 6-4 = 2 para invertir los ultimos dos numeors 
"""
    def reverseK(self, k):
        if k <= 1:  # si k es 1 o menos devuelve la lista igual
            print("k tiene que ser mayor que 1")
            return SList2
       
        if k > len(self):  # si k es mayor que la longitud de la lista, iguala k al size para invertir toda la lista
            k = self._size
           
        current = self._head
        current2 = self._head
       
        listaux = SList()  # esta es una lista auxiliar para introducir los elementos cambiados
        aux = None
       
        i = 0
        while current or aux: #en este bucle
            aux = listaux._head
            if i<k and current: #añades elementos a la lista auxiliar
                listaux.addFirst(current.elem)
                current = current.next
                i +=1
               
            else:
                current2.elem = aux.elem
                current2 = current2.next
                listaux.removeFirst()
               
                if listaux._size == 0:
                    i = 0
                    aux = None

    def maximumPair(self):   # tarda menos
        if self._size == 0:
            return None
        if self._size == 1:  # si la lista mide 1 el mas grande va a ser ese elemento
            return self._head.elem

        current = self._head

        middle = self._head
        aus = SList()  # vamos a crear una lista auxiliar con los valores a partir de la mitad de la lista, es decir, el segundo valor de cada pareja
        if self._size % 2 == 0:
            for i in range(self._size // 2):  # llegamos hatas el elemeto en la mitad de la lista
                middle = middle.next
        else:  # Si la longitud de la lista es impar,
            for i in range(self._size // 2 + 1):  # llegamos hatas el elemeto en la mitad de la lista +1
                middle = middle.next  # en este caso, como el elemento en self._size // 2 no tiene pareja, no lo vamos a incluir en la lista

        while middle:
            aus.addFirst(middle.elem)  # introducimos los elementos del final de la lista en la lista auxiliar
            middle = middle.next

        current2 = aus._head
        suma = 0  # partimos de que la suma es 0
        while current2:
            if current2.elem + current.elem > suma:  # comprobamos si la suma de los elementos correspondientes de las dos lista es mayor que la suma anterios
                suma = current2.elem + current.elem
            current = current.next
            current2 = current2.next
        if self._size % 2 != 0:  # por último, si la lista es impar, comprobamos si el elemento en la mitad es mayor que la suma
            if current.elem > suma:
                suma = current.elem
        return suma

    """def maximumPair(self):
        if self._size == 0:
            return None
        if self._size == 1:  # si la lista mide 1 el mas grande va a ser ese elemento
            return self._head.elem
        current = self._head
        sum1 = 0
        for i in range(int(self._size / 2)):
            # revisar. complejidad muy alta
            currentF = self._head  # este va a ser el current que empiece en el final y vaya hacia atras
            a = int(
                self._size - 1)  # a es una variable para controlar cuanto tiene que retroceder y empieza en self._size - 1 porque es un range y va del 0 al 10 entonces tiene que empezar en el 10 no en el 11
            while currentF.next and a > i:  # aqui el current empieza en el inicio y va hasta cada vez 1 menos
                currentF = currentF.next
                a -= 1
            sum2 = current.elem + currentF.elem
            if sum2 > sum1:
                sum1 = sum2
            current = current.next
            if self._size % 2 != 0 and i == int(
                    self._size / 2) - 1:  # en este momento comprabamos si el bucle ha llegado al final. Si es así y además el tamoño de la lista es impar, deberá comprobar el valor que se encuentra en medio de la lista
                sum2 = current.elem
                if sum2 > sum1:
                    sum1 = sum2
        return sum1"""

    """def maximumPair(self):  # tarda mas
        if self._size == 1:  # si la lista mide 1 pues el mas grande va a ser ese elemento
            return self.getAt(0)
        current1 = self._head
        sum1 = None
        for i in range(int(self._size/2)):
            currentF = self._head  # este va a ser el current que empiece en el final y vaya hacia atras
            a = int(self._size-1)  # a es una variable para controlar cuanto tiene que retroceder y empieza en self._size - 1 porque es un range y va del 0 al 10 entonces tiene que empezar en el 10 no en el 11
            while currentF.next and a > i:  # aqui el current empieza en el inicio y va hasta cada vez 1 menos
                currentF = currentF.next
                a -= 1
            if current1 == self._head:  # estos ifs con las sumas es para sumar y comparar cada resultado de pares, sefuro que se puede hacer mejor pero no se
                sum1 = currentF.elem + current1.elem
            if sum1 < current1.elem + currentF.elem:
                sum1 = currentF.elem + current1.elem
            if self._size%2 != 0 and self.getAt(int(self._size/2)) > sum1:  # aqui si es imparla lista y el del medio es el mayor que el resultado sea ese numero
                sum1 = self.getAt(int(self._size/2))
            print(current1.elem, currentF.elem)
            print(sum1)
            current1 = current1.next
        return sum1"""


SL = SList2()
SL2 = SList2()
for i in range(3):
    SL2.addFirst(i)
for i in range(5, 0, -1):
    SL.addFirst(i)

print(SL)
print(SL2)
SL.insertList(SL2, 0, 3)

print(SL)
print(SL._size)