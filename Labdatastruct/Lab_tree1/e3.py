class Bst:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.size = 1

    def __str__(self):
        return str(self.data)

    def insert(self, data):
        if self.data is None:
            self.data = data
            return 0
        if data == self.data:
            return 0
        if data < self.data:
            if self.left is None:
                self.left = Bst(data)
                self.size += 1
                return 1
            add = self.left.insert(data)
            self.size += add
            return add
        if self.right is None:
            self.right = Bst(data)
            self.size += 1
            return 1
        add = self.right.insert(data)
        self.size += add
        return add

    def search(self, m):
        point = 0
        if self.data <= m:
            point = 1
        if self.left != None and self.right != None:
            return self.left.search(m)+self.right.search(m)+point
        if self.left != None:
            return self.left.search(m)+point
        if self.right != None and self.data < m:
            return self.right.search(m)+point
        return point
    def printTree(self, level=0):
        if self.right != None:
            self.right.printTree(level + 1)
        print('     ' * level, self.data)
        if self.left != None:
            self.left.printTree(level + 1)

# 4 3 7 1 8 5 9 6 2/5
root = Bst()
inp, p = input('Enter Input : ').split('/')
inp = list(map(int, inp.split()))
for i in inp:
    root.insert(i)
root.printTree()
print('--------------------------------------------------\n%d' % root.search(int(p)))