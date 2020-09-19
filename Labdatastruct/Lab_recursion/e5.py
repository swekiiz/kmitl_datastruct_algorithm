def staircase(n, m):
    if n==0:
        return 'Not Draw!'
    if m == n+1 or -m == n-1:
        return ''
    if n < 0:
        return '_'*(m-1)+'#'*(-n-m+1)+'\n'+staircase(n, m+1)
    return '_'*(n-m)+'#'*m+'\n'+staircase(n, m+1)
print(staircase(int(input("Enter Input : ")), 1))
