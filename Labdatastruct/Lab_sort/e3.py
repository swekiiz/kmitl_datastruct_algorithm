p = input('Enter Input : ')
l = r = a = 1
s = 0
for i in range(len(p)-1):
    if p[i] < p[i+1]:  
        r = 0
        a = 0
    if p[i] > p[i+1]:
        l = 0
        a = 0
    if p[i] == p[i+1]:
        s = 1
if a:
    print('Repdrome')
elif l & s:
    print('Plaindrome')
elif l:
    print('Metadrome')
elif r & s:
    print('Nialpdrome')
elif r:
    print('Katadrome')
else:
    print('Nondrome')