def re(n,path):
    if n == a:
        if sum(map(int,path)) == int(c):
            print(' '.join(path))
            return 1
        return 0
    return re(n+1,path+[b[n]])+re(n+1,path)

c, b = input('Enter Input (Money, Product) : ').split('/')
b = b.split()
a = len(b)
print(re(0,[]))