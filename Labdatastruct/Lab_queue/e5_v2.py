(r, b), x, y, q, n, m, z, i, w = input("Enter Input (Red, Blue) : ").split(), [], [], [], 0, 0, 0, 0, 0
while i < len(b):
    if i < len(b)-2 and b[i] == b[i+1] == b[i+2]:
        q.append(b[i])
        i, m = i+3, m+1
    else:
        y.append(b[i])
        i += 1
i, q, S = 0, q[::-1], '----------TENETTENET----------'
while i < len(r):
    if i < len(r)-2 and r[i] == r[i+1] == r[i+2]:
        if q:
            if q[0] == r[i]:
                z, q = z+1, q[1:]
            else:
                x = x + [r[i], r[i], q.pop(0)]
            i += 2
        else:
            i, n = i + 3, n + 1
    else:
        x.append(r[i])
        i += 1
for p in range(10):
    w = 0
    while w < len(x):
        if w < len(x)-2 and x[w] == x[w+1] == x[w+2]:
            x = x[0:w]+x[w+3:len(x)]
            w, n = w-1, n+1
        w += 1
print("Red Team :\n{}\n".format(len(x)) +(''.join(x[::-1]) if len(x) else 'Empty'))
print('%d Explosive(s) ! ! ! (HEAT)' % (n))
print(f'Blue Team Made (a) Mistake(s) {z} Bomb(s)\n{S}' if z > 0 else S)
print(': maeT eulB\n{}\n'.format(len(y))+(''.join(y) if len(y) else 'ytpmE'))
print("(EZEERF) ! ! ! (s)evisolpxE", m)
