O, o, oo = [], [], 'Empty'
for Q in input("Enter Input : ").split(','):
    if Q.startswith('EN'):
        o.append(Q.split()[1])
    elif Q.startswith('ES'):
        O.append(Q.split()[1])
    else:
        print(O.pop(0) if O else o.pop(0) if o else oo)
