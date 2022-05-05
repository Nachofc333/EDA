from slist import SList, SNode
import sys


class SList2(SList):

    # función que toma un número entero n y devuelve la suma de los n últimos nodos de la lista invocante.
    def sumLastN(self, n):
        result = 0  # variable que almacenará la suma de todos los elementos

        if n < 0:  # si la lista está vacía devuelve None
            result = None

        else:
            if n > self._size:  # si n es mayor que la longitud de la lista sumará todos los elemente de la lista
                n = self._size  # por lo que n será igual a la longitud total de la lista

            current = self._head  # nos permitirá recorrer la lista
            for i in range(self._size - n):  # recorremos la lista hasta la posición correcta dependiendo del valor de n
                current = current.next

            for i in range(n):  # sumamos los últimos n elementos
                result += current.elem
                current = current.next

        return result  # devuelve la suma

    # method for inserting a new node in the middle
    def insertMiddle(self, e):
        current = self._head  # variable que recorrera la lista
        newNode = SNode(e)  # nodo que se va a introducir

        if self._size == 0:  # si la lista está vacía se añade directamente al principio de la lista
            self.addFirst(e)
            return

        elif self._size % 2 == 0:  # si la longitud de la lista es par, insertaremos el elemento en la posición len(self)//2
            for i in range(len(self) // 2 - 1):  # llegamos a la posición len(self)//2. Como nuestra variable current ya está en la primera posición de la lista
                 current = current.next  # hay que realizar el bucle len(self)//2 -1 veces para llegar justo al medio. Sino nos pasaríamos de la mitad de la lista

        else:  # si la longitud de la lista es impar insertaremos el elemento en la posición len(self +1)//2
            for i in range((len(self) + 1) // 2 - 1):  # llegamos a la posición len(self +1)//2. Como nuestra variable current ya está en la primera posición de la lista
                current = current.next  # hay que realizar el bucle len(self +1)//2 -1 veces para llegar justo al medio. Sino nos pasaríamos de la mitad de la lista

        newNode.next = current.next  # Una vez que hemos llegado a la posición deseada,
        current.next = newNode  # introducimos el nuevo nodo enlazándolo con el resto de la lista
        self._size += 1

    # función que introduce una lista desde la posicion start hasta end
    def insertList(self, inputList, start, end):
        if start < 0 or start > end or end >= len(self):  # requisitos por los que la función debe hacer return
            print("Error, start debe ser mayor que cero y menor que end y end debe ser menor que len")
            return

        newcurrent = inputList._head  # variable que recorrerá la lista a introducir
        current = self._head  # variable que recorrerá la lista

        if start > 0:
            for i in range(start - 1):  # bucle para que el current llegue hasta el elemento en la posicion start
                current = current.next

        for i in range(end) if start == 0 else range(end - start + 1):  # este bucle borrará los elementos que hay hasta la posición end
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

    # función que invierte los elementos de una lista en k grupos
    def reverseK(self, k):
        if k <= 1:  # si k es 1 o menos devuelve la lista igual
            print("k tiene que ser mayor que 1")
            return SList2

        if k > len(self):  # si k es mayor que la longitud de la lista hay que invertir toda la lista.
            k = self._size  # por lo que k será igual a la longitud de la lista

        current = self._head  # variables que nos permitirán recorrer la lista
        current2 = self._head
        listaux = SList()  # esta es una lista auxiliar para ir introduciendo los elementos que hay que cambiar
        aux = None
        i = 0  # valor encargado de que se invierten justo k elementos

        while current or aux:  # en este bucle invertiremos los elemtos. Hay que realizarlo hasta que hallamos recorrido toda la lista
            aux = listaux._head  # variable que nos permite recorrer la lista auxiliar

            if i < k and current:  # añadimos nodos al principio de la lista auxiliar.
                listaux.addFirst(current.elem)  # Hay que añadir k, pero si llegamos al final de la lista puede pasar que se añadan menos de k nodos
                current = current.next
                i += 1

            else:  # Una vez que ya hemos añadido los nodos a la lista auxiliar,
                current2.elem = aux.elem  # cambiamos el valor de current2 por el primer elemento de la lista auxiliar
                current2 = current2.next  # después borramos el primer nodo de la lista auxiliar y actualizamos current2
                listaux.removeFirst()  # de esta forma, siempre habrá que cambiar el elemento de current2 por el elemento del primer nodo de la lista auxiliar

                if listaux._size == 0:  # si la lista auxiliar está vacía, cambiamos el valor de i para cambiar otros elementos
                    i = 0
                    aux = None

    # funcion que devuelve el valor maximo de la suma de los elementos equidistantes de una lista
    def maximumPair(self):
        if self._size == 0:  # si la lista está vacía devuelve None.
            return None
        if self._size == 1:  # si la lista mide 1 el más grande es ese elemento.
            return self._head.elem

        current = self._head  # variable que nos permite recorrer la lista
        middle = self._head
        aux = SList()  # vamos a crear una lista auxiliar con los valores a partir de la mitad de la lista, es decir, el segundo valor de cada pareja

        if self._size % 2 == 0:
            for i in range(self._size // 2):  # llegamos hatas el elemeto en la mitad de la lista
                middle = middle.next

        else:  # Si la longitud de la lista es impar,
            for i in range(self._size // 2 + 1):  # llegamos hatas el elemeto en la mitad de la lista +1
                middle = middle.next  # en este caso, como el elemento en self._size // 2 no tiene pareja, no lo vamos a incluir en la lista

        while middle:
            aux.addFirst(middle.elem)  # introducimos los elementos del final de la lista en la lista auxiliar
            middle = middle.next

        current2 = aux._head  # variable que nos permite recorrer la lista auxiliar
        suma = 0  # partimos de que la suma es 0
        while current2:
            if current2.elem + current.elem > suma:  # comprobamos si la suma de los elementos correspondientes de las dos lista es mayor que la suma anterior.
                suma = current2.elem + current.elem  # si es así, modificamos el valor de suma
            current = current.next  # actualizamos los valores de current para seguir recorriendo la lista
            current2 = current2.next

        if self._size % 2 != 0:  # por último, si la lista es impar, comprobamos si el elemento en la mitad es mayor que la suma
            if current.elem > suma:  # en ese caso, modificamos el valor de suma
                suma = current.elem

        return suma  # devolvemos el valor de suma.