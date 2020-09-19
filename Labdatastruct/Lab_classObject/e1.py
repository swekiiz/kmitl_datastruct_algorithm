p = input("Enter String : ")
l, k, a = [-1]*26, 0, []
for i in p:
    if l[ord(i)-97] == -1:
        l[ord(i)-97] = k
        k += 1
    a.append(l[ord(i)-97]);
print(a)