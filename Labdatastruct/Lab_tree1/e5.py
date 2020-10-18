class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)
    def dfspre(self):
        print(self.data, end='')
        if self.left != None:
            self.left.dfspre()
        if self.right != None:
            self.right.dfspre()
    def dfsin(self):
        if self.data in '+-*/':
            print('(',end='')
        if self.left != None:
            self.left.dfsin()
        print(self.data, end='')
        if self.right != None:
            self.right.dfsin()
        if self.data in '+-*/':
            print(')',end='')
    def printTree(self, level=0):
        if self.right != None:
            self.right.printTree(level + 1)
        print('     ' * level, self.data)
        if self.left != None:
            self.left.printTree(level + 1)
n = input('Enter Postfix : ')
s = []
for i in n:
    if i in '+-*/':
        t = Node(i)
        t.right = s.pop()
        t.left = s.pop()
        s.append(t)
    else:
        s.append(Node(i))
root = s.pop()
print('Tree :')
root.printTree()
print('--------------------------------------------------\nInfix : ', end='')
root.dfsin()
print('\nPrefix : ', end='')
root.dfspre()
