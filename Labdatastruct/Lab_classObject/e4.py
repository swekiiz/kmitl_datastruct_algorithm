a, l = list(map(int, input("Enter Your List : ").strip().split())), []
if len(a) <= 2:
    print('Array Input Length Must More Than 2')
else:
    for i, it in enumerate(a[:]):
        for j, jt in enumerate(a[i+1:]):
            for k in a[j+1:]:
                if 0 == it + jt + k:
                    l.append([it, jt, k])
    print(l)
