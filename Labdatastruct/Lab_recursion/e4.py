def pp(r, s):
    s.append(r.pop())
    print('|  |  |')
    print('\n'.join(map(lambda x: '  '.join(['|' if len(a[0]) <= x else a[0][x], '|' if len(a[1]) <= x else a[1][x], '|' if len(a[2]) <= x else a[2][x]])[::-1], range(q)))[::-1])
def move(n, A, B, C):
    if n != 0:
        move(n-1, A, C, B)
        print(f'move {n} from  {A} to {C}')
        pp(a[ord(A)-65], a[ord(C)-65])
        move(n-1, B, A, C)
    return ''
q = int(input("Enter Input : "))
a = [[str(i) for i in range(q, 0, -1)], [], []]
print('|  |  |')
print('\n'.join(map(lambda x: '  '.join(['|' if len(a[0]) <= x else a[0][x], '|' if len(a[1]) <= x else a[1][x], '|' if len(a[2]) <= x else a[2][x]])[::-1], range(q)))[::-1])
print(move(q, "A", "B", "C"))