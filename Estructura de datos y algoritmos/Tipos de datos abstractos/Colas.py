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


Q = Queue()
for i in range(10):
    Q.enqueue(i)
print(Q)

print(Q.dequeue())
print(Q)
