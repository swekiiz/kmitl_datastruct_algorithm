def g(a):
    for i in a:
        if i in "qwertyuiopasdfghjklzxcvbnm":
            return i
def s(p):
    for i in range(len(p)):
        for j in range(len(p) - i - 1):
            if g(p[j]) > g(p[j+1]):
                p[j], p[j+1] = p[j+1], p[j]


l = input('Enter Input : ').split()
s(l)
print(*l)