a, b = input('Enter Input : ').split('/')
a, b = sorted([*map(int, a.split())]), [*map(int, b.split())]
for i in b:
    l, r = 0, len(a)-1
    while l <= r:
        m = l + (r-l)//2
        if a[m] == i + 1:
            print(i + 1)
            break
        if a[m] < i + 1:
            l = m+1
        else:
            r = m-1
    else:
        print('No First Greater Value' if l == len(a) else a[l])