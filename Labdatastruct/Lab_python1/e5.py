ls = list(map(int, input('*** Fun with countdown ***\nEnter List : ').split()))
def f(x):
    if ls[x] == 1:
        j = x
        while(j != 0 and ls[j] + 1 == ls[j-1]):
            j -= 1
        return ls[j:x+1]
s = [*filter(lambda x: x != None, [*map(f, [i for i in range(len(ls))])])]
print([len(s), s])