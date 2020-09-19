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
        return '->'.join(s.strip().split())

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


l, f = LinkedList(), True
for i in input("Enter Input : ").split(','):
    if f:
        f = not f
        for j in i.split():
            l.append(j)
    else:
        t = i.split(':')
        if 0 <= int(t[0]) <= l.length():
            l.insert(int(t[0]), t[1])
            print('index = {} and data = {}'.format(t[0].strip(),t[1]))
        else:
            print('Data cannot be added')
    print('List is empty' if l.isEmpty() else 'link list : %s' % l)
