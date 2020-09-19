def yee(lst, t, i):
    while i < len(lst[:]):
        if lst[i] == lst[i-1] and lst[i] == lst[i-2]:
            t.append(i)
            i += 2
        i += 1
    return t
(r, b), h, f, z = input("Enter Input (Red, Blue) : ").split(), [], [], 0
h, f, x, y = yee(lst=r, t=[], i=2), yee(lst=b[::-1], t=[], i=2), r[:], b[::-1]
s, c, p = '----------TENETTENET----------', len(h), 0
for i in range(len(h)):
    print("before : ", x, y, '\n', h, f)
    if i >= min(len(h), len(f)):
        x = x[0:h[i]-2]+x[h[i]+1:len(x)]
        h, p = [j-3 for j in h], i
    elif x[h[i]] == y[f[i]]:
        x, y, z = x[0:h[i]-1]+x[h[i]+1:len(x)], y[0:f[i]-2]+y[f[i]+1:len(y)], z+1
        h, f, p = [j-2 for j in h], [j-3 for j in f], i
    else:
        x, y, c = x[0:h[i]]+y[f[i]]+x[h[i]:], y[0:f[i]-2]+y[f[i]+1:len(y)], c-1
        h, f, p = [j+1 for j in h], [j-3 for j in f], i
    print(" after : ", x, y, '\n', h, f)
while p < len(f) - 1:
    y = y[0:f[p+1]-2]+y[f[p+1]+1:len(y)]
    f, p = [j-3 for j in f], p+1
w = '{:d} Explosive)s( ! ! ! )FREEZE('.format(len(f))[::-1]
d = 'Blue Team Made (a) Mistake(s) %d Bomb(s)\n' % (z) if z > 0 else ''
print(f"""Red Team :\n{len(x)}\n{x[::-1] if len(x) else 'Empty'}
{c-z} Explosive(s) ! ! ! (HEAT)\n{d+s}\n: maeT eulB\n{len(y)}\n{y[::-1] if len(y) else 'ytpmE'}\n{w}""")
