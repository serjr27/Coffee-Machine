class Stack():

    def __init__(self):
        self.s = list()
        self.i = -1

    def push(self, el):
        self.s.append(el)
        self.i += 1

    def pop(self):
        temp = self.s[self.i]
        self.s.pop(self.i)
        self.i -= 1
        return temp

    def peek(self):
        return self.s[self.i - len(self.s)]

    def is_empty(self):
        return self.i == -1
