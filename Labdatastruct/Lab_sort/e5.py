def com(a, b):
    if len(a) == len(b):
        i = 0
        while i < len(b) and a[i] == b[i]:
            i += 1
        return a[i] < b[i]
    return len(a) < len(b)


def pp(a, b):
    return a < b


def sss(p, c):
    for i in range(len(p)):
        for j in range(len(p) - i - 1):
            if not c(p[j], p[j+1]):
                p[j], p[j+1] = p[j+1], p[j]


def re(x):
    if x == len(b):
        if sum(s) == a:
            l.append(s[:])
        return
    s.append(b[x])
    re(x+1)
    s.pop()
    re(x+1)


(a, b) = input('Enter Input : ').split('/')
a, b, s, l = int(a), list(map(int, b.split())), [], []
sss(b, pp)
re(0)
sss(l, com)
for i in l:
    print(i)
if not l:
    print('No Subset')