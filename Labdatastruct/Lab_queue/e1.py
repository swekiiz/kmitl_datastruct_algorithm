Q = []
for t in input("Enter Input : ").split(','):
    if t[0] == 'E': Q.append(t.split(' ')[1])
    print(len(Q) if t[0] == 'E' else Q.pop(0)+' 0' if Q else -1)
if not Q: print('Empty')
while Q: print(Q.pop(0)+' ', end='')