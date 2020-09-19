l, s, h = input("Enter Input : ").split(','), [], 0
for i in l:
    if i[0] == 'A':
        t = int(i.split()[1])
        s.append(t + 2*h if t % 2 else max(t - 1*h, 1))
    elif i[0] == 'B':
        c, m = 0, 0
        for i in s[::-1]:
            if i > m:
                c, m = c+1, i
        print(c)
    elif i[0] == 'S':
        t =  []
        for i in s[::-1]:
            i = i + 2 if i % 2 else max(i - 1, 1)
            t.append(i)
        s = t[::-1]
