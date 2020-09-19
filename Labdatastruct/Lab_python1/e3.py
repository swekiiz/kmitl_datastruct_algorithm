int(input('*** Election ***\nEnter a number of voter(s) : '))
r = list(map(int, input().strip().split()))
r = list(filter(lambda x: x > 0 and x < 21, r))
print('*** No Candidate Wins ***' if not r else max(set(r), key=r.count))