class queue:
    def __init__(self):
        self.q = []

    def push(self, x):
        self.q.append(x)

    def pop(self):
        if not self.empty():
            f = self.q[0]
            self.q = self.q[1:]
            return f

    def empty(self):
        return True if len(self.q) == 0 else False

    def front(self):
        return self.q[0]

    def size(self):
        return len(self.q)