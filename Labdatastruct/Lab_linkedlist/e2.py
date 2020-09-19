class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def __str__(self):
        cr, s = self.head, ''
        while cr.next != None:
            cr = cr.next
            s += str(cr) + ' '
        return '->'.join(s.strip().split())

    def str_reverse(self):
        cr, s = self.head, ''
        while cr.next != None:
            cr = cr.next
        s += str(cr) + ' '
        while cr.prev != None and cr.prev.data != None:
            cr = cr.prev
            s += str(cr) + ' '
        if s.startswith('None'):
            s = ''
        return '->'.join(s.strip().split())

    def isEmpty(self):
        return self.size == 0

    def append(self, data):
        nn, cr = Node(data), self.head
        while cr.next != None:
            cr = cr.next
        nn.prev = cr
        cr.next, self.size = nn, self.size+1

    def insert(self, index, data):
        nn, cr, c = Node(data), self.head, 0
        while c < index:
            cr, c = cr.next, c+1
        nn.next = cr.next
        nn.prev = cr
        if cr.next != None:
            cr.next.prev = nn
        cr.next, self.size = nn, self.size + 1

    def remove(self, data):
        cr, c = self.head, -1
        while cr != None and cr.data != data:
            cr, c = cr.next, c+1
        if cr == None:
            return None
        cr.prev.next = cr.next
        if cr.next != None:
            cr.next.prev = cr.prev
        self.size = self.size - 1
        return (cr.data, c)

    def length(self):
        return self.size


l = DoublyLinkedList()
for i in input("Enter Input : ").split(','):
    i = i.strip()
    if i.startswith('Ab'):
        l.insert(0, i[3:])
    elif i.startswith('A'):
        l.append(i[2:])
    elif i.startswith('R'):
        p = l.remove(i[2:])
        print('Not Found!' if p == None else 'removed : {} from index : {}'.format(p[0], p[1]))
    elif i.startswith('I'):
        t = i[2:].split(':')
        if 0 <= int(t[0]) <= l.length():
            l.insert(int(t[0]), t[1])
            print('index = {} and data = {}'.format(t[0], t[1]))
        else:
            print('Data cannot be added')
    print('linked list : %s' % l)
    print('reverse : %s' % l.str_reverse())
