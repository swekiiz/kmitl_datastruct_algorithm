def length(txt):
    if txt == '':
        return ('', 0)
    t = length(txt[:-1])
    return (t[0] + txt[-1] + ('*', '~')[t[1] & 1], t[1] + 1)
o = length(input("Enter Input : "))
print(o[0], f'\n{o[1]}')
