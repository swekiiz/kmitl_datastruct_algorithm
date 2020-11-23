def dfs(x, y):
    s.append(x); ch[x] = True
    if x == y:
        ans.append(' -> '.join(s))
    else:
        for i in l[x]:
            if not ch[i]:
                dfs(i, y)
    ch[x] = False; s.pop()
ch, l, t, s, ans, (a, b) = dict(), dict(), [0, 0], [], [], input('Enter Input : ').split('/')
for i in a.split(','):
    t[0], t[1] = i.split()
    for j in range(2):
        if t[j & 1] in l.keys():
            l[t[j & 1]].append(t[(j+1) & 1])
        else:
            l[t[j & 1]] = [t[(j+1) & 1]]
        if t[j & 1] not in ch:
            ch[t[j & 1]] = False
dfs(*b.split())
print((f'All possible path from {b.split()[0]} to {b.split()[1]} :\n' + '\n'.join(sorted(ans, key=lambda x:(len(x), x))) if len(ans) else f'{b.split()[0]} can\'t go to {b.split()[1]}'))