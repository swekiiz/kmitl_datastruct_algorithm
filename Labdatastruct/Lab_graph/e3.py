import heapq
a = dict()
def dijkstra(u, v):
    ch = {i: False for i in a.keys()}
    d = {i: int(2e9) for i in a.keys()}
    p = {i: [] for i in a.keys()}
    d[u], Q = 0, []
    p[u].append(u)
    heapq.heappush(Q, [0, u])
    while Q:
        c = heapq.heappop(Q)
        ch[c[1]] = True
        if c[1] == v:
            break
        for n in sorted(a[c[1]]):
            if not ch[n[1]] and d[n[1]] > d[c[1]] + n[0]:
                d[n[1]] = d[c[1]] + n[0]
                p[n[1]] = p[c[1]] + [n[1]]
                heapq.heappush(Q, [d[n[1]], n[1]])
    return p[v]
(t, q) = input('Enter : ').split('/')
for i in t.split(','):
    u, w, v = i.split()
    w = int(w)
    if u in a.keys():
        a[u].append([w, v])
    else:
        a[u] = [[w, v]]
    if v not in a.keys():
        a[v] = []
for i in q.split(','):
    try:
        sp = dijkstra(*i.split())
        if sp:
            print(' to '.join(i.split()), ':', '->'.join(sp))
        else:
            print('Not have path :', ' to '.join(i.split()))
    except:
        print('Not have path :', ' to '.join(i.split()))