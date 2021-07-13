import sys 
sys.stdin = open('input.txt', 'rt')

# 숫자를 뒤집는 함수 reverse 하나
# 소수인지 아닌지를 확인하는 함수 isPrime 하나 


n = int(input())
a = map(int,input().split())

def reverse(x):
    res =0
    while x > 0:
        t = x % 10 
        res = res*10 +t
        x = x//10
    return res
    

def isPrime(x):
    if x ==1:
        return False
    for i in range(2, x//2+1):
        x % i == 0
        return False
    else :
        return True
        

for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end =' ')