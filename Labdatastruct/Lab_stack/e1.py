
def main():
    s = input('Enter Input : ')
    l = []
    d = {'}': '{', ']': '[', ')': '('}

    for i in s:
        if i in '{[(':
            l.append(i)
        elif i in '})]':
            if len(l) == 0:
                print('Parentheses : Unmatched ! ! !')
                return
            if l[-1] != d[i]:
                print('Parentheses : Unmatched ! ! !')
                return
            else:
                l = l[:-1] 
    if len(l) != 0:
        print('Parentheses : Unmatched ! ! !')
    else:
        print('Parentheses : Matched ! ! !')


main()
