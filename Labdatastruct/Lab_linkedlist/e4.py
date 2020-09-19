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
        self.cur = self.head
    def __str__(self):
        cr, s = self.head, ''
        if self.cur == self.head:
            s += '| '
        while cr.next != None:
            cr = cr.next
            s += str(cr) + ' '
            if cr == self.cur:
                s += '| '
        return ' '.join(s.strip().split())
    def ibc(self, data):
        nn = Node(data)
        nn.next = self.cur.next
        if self.cur.next != None:
            self.cur.next.prev = nn
        nn.prev = self.cur
        self.cur.next = nn
        self.cur, self.size = nn, self.size + 1
    def sl(self):
        if self.cur.prev != None:
            self.cur = self.cur.prev
    def sr(self):
        if self.cur.next != None:
            self.cur = self.cur.next
    def dl(self):
        if self.cur != self.head and self.cur.prev != None:
            self.cur.prev.next = self.cur.next
            if self.cur.next != None:
                self.cur.next.prev = self.cur.prev
            self.cur = self.cur.prev
            self.size += -1
    def dr(self):
        if self.cur.next != None:
            cr = self.cur.next
            cr.prev.next = cr.next
            if cr.next != None:
                cr.next.prev = cr.prev
            self.size += -1
l = DoublyLinkedList()
for i in input('Enter Input : ').split(','):
    if i[0] == 'I':
        l.ibc(i.split()[1])
    elif i[0] == 'L':
        l.sl()
    elif i[0] == 'R':
        l.sr()
    elif i[0] == 'B':
        l.dl()
    elif i[0] == 'D':
        l.dr()
print(l)