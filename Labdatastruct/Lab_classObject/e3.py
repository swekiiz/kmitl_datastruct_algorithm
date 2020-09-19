def odd_even(arr, s):
    return [arr[i] for i in range(len(arr)) if i % 2 == ['Odd', 'Even'].index(s)]
l = input('*** Odd Even ***\nEnter Input : ').split(',')
u = odd_even(l[1].split() if l[0] == 'L' else list(l[1]), l[2])
print(''.join(u) if l[0] == 'S' else u)
