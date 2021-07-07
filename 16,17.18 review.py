

import sys
sys.stdin = open('input.txt','rt')

n = int(input())
a = list(map(int, input().split()))

avg = round(sum(a)/n)
min = 2147000000

for idx,s in enumerate(a):
    tmp = abs(avg-s)
    if tmp < min:
        min = tmp
        score = s
        res = idx +1
    elif tmp == min:
        if s > score:
            score = s
            res = idx+1
print(avg,res)