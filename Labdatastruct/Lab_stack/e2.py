l = [i.split() for i in input('Enter Input : ').split(',')]
s = []
for i in l:
    while not not s and int(s[-1][0]) < int(i[0]):
        print(s[-1][1])
        s = s[:-1]
    s.append(i)
