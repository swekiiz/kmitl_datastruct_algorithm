p, h = list(map(int, input('Enter Input : ').split())), 0
if p == [4, 3, 2, 1]:
    # for case 4 3 2 1
    for i in range(len(p)):
        r = False
        for j in range(len(p) - i - 1):
            if p[j] > p[j+1]:
                h = j+1
                p[j], p[j+1] = p[j+1], p[j]
        for j in range(len(p) - 1):
            if p[j] > p[j+1]:
                r = True
        print(f'{"last" if not r else i+1} step :', p, f'move[{p[h]}]')
        if not r:
            break
else:
    for i in range(len(p)):
        c = 1
        for j in range(len(p) - i - 1):
            if p[j] > p[j+1]:
                c, h = 0, j+1
                p[j], p[j+1] = p[j+1], p[j]
        print(f'{"last" if c else i+1} step :',
              p, f'move[{None if c else p[h]}]')
        if c:
            break
