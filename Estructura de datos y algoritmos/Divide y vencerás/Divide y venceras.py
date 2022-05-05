"""
Consiste en estrategias recursivas e iterativas para dividir los algoritmos del problema en subproblemas pequeños,
vencer esas soluciones y finalmente combinarlas
Mergesort:
Ordenar una lista hasta que esté ordenada, longitud 1
Quicksort:
Ordenar una lista pero ordenando areas de la lista en particiones
"""
import random


def max_value(L):
    if len(L) == 0:
        return
    if len(L) == 1:
        return L[0]
    L1 = L[:len(L)//2]
    L2 = L[len(L)//2:]
    return max(max_value(L1), max_value(L2))

def mergesort(L):
    if len(L) == 0:
        return L
    if len(L) == 1:
        return L
    L1 = mergesort(L[:len(L) // 2])
    L2 = mergesort(L[len(L) // 2:])
    L[:] = merge(L1, L2)
    return L
def merge(L1, L2):
    i = 0
    j = 0
    L = []
    while i < len(L1) and j < len(L2):
        if L1[i]<L2[j]:
            L.append(L1[i])
            i += 1
        else:
            L.append(L2[j])
            j += 1
        while i < len(L1):
            L.append(L1[i])
            i += 1
        while j < len(L2):
            L.append(L2[j])
            j += 1
    return L

def quicksort():
    ...
L = []

for i in range(8):
    L.append(random.randint(0, 100))

print(mergesort(L))
print(max_value(L))