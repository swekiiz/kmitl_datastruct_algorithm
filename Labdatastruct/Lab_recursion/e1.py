def r(p, t):
    if t == 0:
        return p[0]
    return max(p[t], r(p, t-1))


p = list(map(int, input('Enter Input : ').split()))
print('Max :', r(p, len(p)-1))
