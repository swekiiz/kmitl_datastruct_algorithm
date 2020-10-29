def dp(n):
    if n >= len(bst):
        return 0
    bst[n] = dp(2*n+1) + dp(2*n+2) + bst[n]
    return bst[n]
bst, b = input('Enter Input : ').split('/')
bst, b = list(map(int, bst.split())), b.split(',')
print(dp(0))
for x, y in map(lambda t: list(map(int, t.split())), b):
    s = (('<', '>'), ('=', ''))[bst[x] == bst[y]][bst[x] > bst[y]]
    print(f'{x}{s}{y}')
