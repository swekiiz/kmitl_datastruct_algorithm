def dfs(x):
    if ch[x]:
        return
    ch[x] = True
    print(chr(x+65), end=' ')
    for i in sorted(l[x]):
        if not ch[i]:
            dfs(i)


def bfs(x):
    Q = [x]
    while Q:
        x = Q.pop(0)
        if ch[x]:
            continue
        ch[x] = True
        print(chr(x+65), end=' ')
        for i in sorted(l[x]):
            if not ch[i]:
                Q.append(i)


p = input('Enter : ').split(',')
l, m, Q = [[] for _ in range(26)], 2e9, []
for k in p:
    i, j = k.split()
    l[ord(i)-65].append(ord(j)-65)
    l[ord(j)-65].append(ord(i)-65)
print('Depth First Traversals : ', end='')
ch = [False for _ in range(26)]
for i in range(len(l)):
    if l[i]:
        dfs(i)
print('\nBredth First Traversals : ', end='')
ch = [False for _ in range(26)]
for i in range(len(l)):
    if l[i]:
        bfs(i)
