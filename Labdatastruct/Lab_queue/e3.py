o = input('Enter Input : ').split('/')
Q = o[0].split()
for i in o[1].split(','):
    Q.pop(0) if i[0] == 'D' else Q.append(i.split()[1])
print('Duplicate' if any(list(map(lambda x: Q.count(x) != 1, Q))) else 'NO Duplicate')
