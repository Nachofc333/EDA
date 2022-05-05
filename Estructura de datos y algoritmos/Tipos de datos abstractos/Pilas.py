class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        text = str(self.items)
        return text

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, e):
        self.items.append(e)

    def pop(self):
        if self.isEmpty():
            print("lista vacia")
        else:
            return self.items.pop()

    def top(self):
        if self.isEmpty():
            print("lista vacia")
        else:
            return self.items[-1]

S = Stack()

for i in range(6):
    S.push(i)
print(S)

S.pop()
print(S.top())

def reverse(word):
    a = Stack()
    w = ""
    for i in word:
        a.push(i)
    while not S.isEmpty():
        w += a.pop()
    return w

print(reverse("Hola"))
