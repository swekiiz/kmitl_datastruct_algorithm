p, h = list(map(int, input('Enter Input : ').split())), 0
for i in range(len(p)):
    q = c = 1
    for j in range(len(p) - i - 1):
        if p[j] > p[j+1]:
            c, h = 0, j+1
            p[j], p[j+1] = p[j+1], p[j]
    if i == len(p) - 2:
        q = 0
    print(f'{"last" if c or not q else i+1} step :',
          p, f'move[{None if c else p[h]}]')
    if c or not q:
        break
