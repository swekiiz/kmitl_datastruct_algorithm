l, s = input("Enter Input : ").split(','), []
for i in l:
    if i[0] == 'A':
        while not not s and s[-1] <= int(i.split()[1]):
            s = s[:-1]
        s.append(int(i.split()[1]))
    elif i[0] == 'B':
        print(len(s))