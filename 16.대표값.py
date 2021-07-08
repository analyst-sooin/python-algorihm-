import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())
a = list(map(int, input().split()))
print('asfasf')
avg = round(sum(a) / n)
min = 2147000000
for idx , s in enumerate(a):
    dist = abs(s - avg)
    if dist < min:
        min = dist
        score = s
        res = idx +1
    elif dist == min:
        if s > score:
            score = s
            res = idx +1
