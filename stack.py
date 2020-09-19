class stack:
    def __init__(self):
        self.s = []

    def push(self, x):
        self.s.append(x)

    def pop(self):
        if not self.empty():
            return self.s.pop()

    def empty(self):
        return True if len(self.s) == 0 else False

    def top(self):
        return self.s[-1]

    def size(self):
        return len(self.s)