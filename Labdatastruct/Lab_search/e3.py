class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)
class hash:
    def __init__(self, s, m):
        self.max_size = s
        self.table = [None] * s
        self.max_collision = m
        self.size = 0
    def insert(self, defkey, value):
        key = sum(map(ord, list(defkey)))
        i, c = key % self.max_size, 1
        st = i
        while self.table[i] != None:
            print(f'collision number {c} at {i}')
            if c == self.max_collision:
                print('Max of collisionChain')
                break
            i = (st + c*c) % self.max_size
            c += 1
        else:
            self.table[i], self.size = (defkey, value), self.size+1
        for i in range(1, self.max_size+1):
            print('#{:d}	{:s}'.format(
                i, str(self.table[i-1]).replace("'", '')))
    def is_full(self):
        return self.size == self.max_size
a, b = input(' ***** Fun with hashing *****\nEnter Input : ').split("/")
s, m = a.split()
h = hash(int(s), int(m))
for i in b.split(','):
    h.insert(*i.split())
    print('-'*27)
    if h.is_full():
        print('This table is full !!!!!!')
        break