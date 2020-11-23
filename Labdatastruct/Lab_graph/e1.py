p = input('Enter : ').split(',')
a, m, l = [[0 for _ in range(200)] for _ in range(200)], 0, set()
for k in p:
    i, j = k.split()
    l.add(i)
    l.add(j)
    a[ord(i)-100][ord(j)-100] = 1
v = sorted([*l])
print("   ", "  ".join(map(str, v)))
for i in v:
    print(i, ': ', end='')
    for k, j in enumerate(v):
        print(a[ord(i)-100][ord(j)-100], end=(', ' if k != len(v)-1 else '\n'))