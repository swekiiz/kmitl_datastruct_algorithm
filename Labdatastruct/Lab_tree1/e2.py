class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return self.root
        cur = self.root
        while cur is not None:
            if data < cur.data:
                if cur.left is None:
                    cur.left = Node(data)
                else:
                    cur = cur.left
            elif data > cur.data:
                if cur.right is None:
                    cur.right = Node(data)
                else:
                    cur = cur.right
            else:
                return self.root
        
        return self.root
    def getMin(self):
        cur = self.root
        while cur.left != None:
            cur = cur.left
        return cur.data
    def getMax(self):
        cur = self.root
        while cur.right != None:
            cur = cur.right
        return cur.data
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------\nMin : {}\nMax : {}'.format(T.getMin(),T.getMax()))