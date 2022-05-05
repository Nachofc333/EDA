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

def balancePar(exp):
    S = Stack()

    for i in exp:
        if i == "(":
            S.push(i)
        elif i == ")":
            S.pop()






