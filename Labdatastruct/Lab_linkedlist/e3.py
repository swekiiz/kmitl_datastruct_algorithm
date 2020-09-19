class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def __str__(self):
        cr, s = self.head, ''
        while cr.next != None:
            cr = cr.next
            s += str(cr) + ' '
        return ' '.join(s.strip().split())

    def re(self):
        cr, s = self.head, ''
        while cr.next != None:
            cr = cr.next
            s += str(cr)[::-1] + ' '
        return ' '.join(s.strip().split())[::-1]

    def isEmpty(self):
        return self.size == 0

    def append(self, data):
        nn, cr = Node(data), self.head
        while cr.next != None:
            cr = cr.next
        cr.next, self.size = nn, self.size+1

    def insert(self, index, data):
        nn, cr, c = Node(data), self.head, 0
        while c < index:
            cr, c = cr.next, c+1
        nn.next = cr.next
        cr.next, self.size = nn, self.size + 1

    def length(self):
        return self.size


n, m = LinkedList(), LinkedList()
t = input('Enter Input (L1,L2) : ').split()
for i in t[0].split('->'):
    n.append(i)
for i in t[1].split('->'):
    m.append(i)
print('L1    :', n)
print('L2    :', m)
print('Merge :', n, m.re())
