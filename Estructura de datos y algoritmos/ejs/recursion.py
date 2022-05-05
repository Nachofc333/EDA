import random

def sumN(n):
    if n == 0:
        return 0
    return n + sumN(n-1)

def factorial(n):
    if n==0 or n == 1:
        return 1
    return n * factorial(n-1)

def mult(a, b):
    if b == 0:
        return 0
    return a + mult(a, b-1)

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)

def sumL(L:list):  # NO VA
    if len(L) == 0:
        return 0
    return L[0] + sumN(L[1:])

def palin(w:str):
    if len(w)==0:
        return True
    return w[0] == w[-1] and palin(w[1:-1])

def are_adyacent(w, a, b):
    if len(w) == 0:
        return False
    return (w[0] == a and w[1] == b) or are_adyacent(w[1:], a, b)

def invertirlista(L):
    if len(L) == 0:
        return []
    return [L[-1]] + invertirlista(L[:-1])

def ordenarlist(L):
    if len(L) == 0:
        return L
    min = L[0]
    for i in L:
        if i < min:
            min = i
    x = L.remove(min)
    return [x]+ordenarlist(L)

def busquedaBinaria(L, x):
    if len(L) == 0:
        return L[0]==x
    return busquedaBinaria(L[:len(L)//2],x) or busquedaBinaria(L[len(L)//2], x)





L = [1,2,3]

print(invertirlista(L))
