class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, e):
        self.items.insert(0, e)

    def dequeue(self):
        if self.isEmpty():
            print("Error")
        else:
            return self.items.pop()

    def front(self):
        if self.isEmpty():
            print("Error")
        else:
            return self.items[0]

def josephus(n, s):
    cola = Queue()
    for i in range(n):
        cola.enqueue(i+1)
    while len(cola) > 1:
        c = 0
        while c < s:
            x = cola.dequeue()
            cola.enqueue(x)
            c += 1
        cola.dequeue()
    return cola

print(josephus(10, 2))