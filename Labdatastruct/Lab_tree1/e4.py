class Bst:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    def insert(self, data):
        if self.data is None:
            self.data = data
        elif data < self.data:
            if self.left is None:
                self.left = Bst(data)
            else:
                self.left.insert(data)
        elif self.data < data:
            if self.right is None:
                self.right = Bst(data)
            else:
                self.right.insert(data)
    def dfspre(self):
        print(self.data, end=' ')
        if self.left != None:
            self.left.dfspre()
        if self.right != None:
            self.right.dfspre()
    def dfsin(self):
        if self.left != None:
            self.left.dfsin()
        print(self.data, end=' ')
        if self.right != None:
            self.right.dfsin()
    def dfspost(self):
        if self.left != None:
            self.left.dfspost()
        if self.right != None:
            self.right.dfspost()
        print(self.data, end=' ')
    def bfs(self):
        q = [self]
        while q:
            cur = q.pop(0)
            print(cur.data, end=' ')
            if cur.left != None:
                q.append(cur.left)
            if cur.right != None:
                q.append(cur.right)
n = list(map(int,input('Enter Input : ').strip().split()))
root = Bst()
for i in n:
    root.insert(i)
print('Preorder : ',end='')
root.dfspre()
print('\nInorder : ',end='')
root.dfsin()
print('\nPostorder : ',end='')
root.dfspost()
print('\nBreadth : ',end='')
root.bfs()