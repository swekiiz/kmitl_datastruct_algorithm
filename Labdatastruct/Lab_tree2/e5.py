def insert(n):
    global sz
    hp[sz] = n
    i = sz
    while i != 0 and hp[(i-1)//2] > hp[i]:
        hp[(i-1)//2], hp[i] = hp[i], hp[(i-1)//2]
        i = (i-1)//2
    sz += 1
def pop():
    global sz
    t = hp[0]
    hp[0] = hp[sz-1]
    hp[sz-1] = 1 << 31
    i = 0
    while hp[i] > hp[i*2+1] or hp[i] > hp[i*2+2]:
        if hp[i*2+1] < hp[i*2+2]:
            hp[i*2+1], hp[i] = hp[i], hp[i*2+1]
            i = i*2+1
        else:
            hp[i*2+2], hp[i] = hp[i], hp[i*2+2]
            i = i*2+2
    sz -= 1
    return t
hp, sz = [1 << 31] * 1000, 0
a, b = input('Enter Input : ').split('/')
b = list(map(int, b.split()))
for i in range(int(a)):
    insert(i+1)
for i in range(len(b)):
    print(f'Customer {i+1} Booking Van {hp[0]%1000} | {b[i]} day(s)')
    insert(pop()+b[i]*1000)