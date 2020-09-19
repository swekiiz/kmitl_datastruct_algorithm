o, q = input('Enter Input : ').split('/'), []
d = {k: v for v, k in map(lambda x: x.split(), o[0].split(','))}
for n in o[1].split(','):
    if n[0] == 'E':
        if d[n.split()[1]] not in {x[0] for x in q}:
            q.append([d[n.split()[1]], [n.split()[1]]])
        else:
            q[[i for i in range(len(q)) if q[i][0] == d[n[2:]]][0]][1].append(n[2:])
    elif n[0] == 'D':
        print(q[0][1].pop(0) if q else 'Empty')
        if q and not q[0][1]:
            q.pop(0)