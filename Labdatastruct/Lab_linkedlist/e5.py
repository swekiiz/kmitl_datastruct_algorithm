class Node:
    def __init__(self, data):
        self.data, self.next = data, None
class LL:
    def __init__(self):
        self.size, self.head = 0, None
    def __str__(self):
        if self.size == 0: return ''
        t, c = str(self.head.data) + ' ', self.head
        while c.next != None:
            t += str(c.next.data) + ' '
            c = c.next
        return t
    def add(self, a):
        n, self.size = Node(a), self.size + 1
        if self.size == 1: self.head = n
        else:
            c = self.head
            while c.next != None: c = c.next
            c.next = n
def st(i, j, k):
    for x in range(10):
        for xx in sorted(i[x]):
            j[~k & 1][x].add(xx)
a = list(map(int, input("Enter Input : ").split()))
print('-'*60 + '\nRound : 1')
s, l, t, c, p = len(a), [[LL() for _ in range(10)], []], [[] for _ in range(10)], 10, 1
for i in a: t[(-i if i < 0 else i) % 10].append(i)
st(t, l, 1)
print(''.join(map(lambda x: f'{x} : {l[0][x]}' + ('' if x == 9 else '\n'), range(10))))
while s != l[~p & 1][0].size:
    l[p & 1], t = [LL() for _ in range(10)], [[] for _ in range(10)]
    for i in l[~p & 1]:
        for j in map(int, str(i).split()):
            t[((-j if j < 0 else j)//c) % 10].append(j)
    st(t, l, p-1)
    p, c = p+1, c*10
    print('-'*60+f'\nRound : {p}\n'+''.join(map(lambda x:f'{x} : {l[~p&1][x]}'+('' if x==9 else '\n'), range(10))))
print('-'*60 + "\n{} Time(s)".format(p-1))
print('Before Radix Sort :', ' -> '.join(map(str, a)))
print('After  Radix Sort :', str(l[~p & 1][0]).rstrip().replace(' ', ' -> '))