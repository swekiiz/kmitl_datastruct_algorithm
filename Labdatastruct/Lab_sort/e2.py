def ss(n, k, m, i):
    if n == len(p) - 1:
        return
    if k == len(p) - n:
        p[i], p[len(p) - n - 1] = p[len(p) - n - 1], p[i]
        if len(p) - n - 1 != i:
            print(f'swap {p[i]} <-> {p[len(p) - n - 1]} : {p}')
        ss(n+1, 0, -1, -1111111111)
        return
    if p[k] > m:
        ss(n, k+1, p[k], k)
    else:
        ss(n, k+1, m, i)
p = list(map(int, input('Enter Input : ').split()))
ss(0, 0, -1, 0)
print(p)
