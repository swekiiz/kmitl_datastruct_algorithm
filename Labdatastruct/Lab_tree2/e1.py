class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = self.right = None
    def insert(self,data):
        if self.data is None:
            self.data = data
        if data < self.data:
            print('L',end='')
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif self.data < data:
            print('R',end='')
            if self.right == None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        

bst = Node()

for i in list(map(int,input('Enter Input : ').strip().split())):
    bst.insert(i)
    print('*')
