

a=1
A=2
A1=3
#2b=4
print(a, A, A1)
'''
변수명 정하기
 1) 영문과 숫자, _로 이루어진다.
 2) 대소문자를 구분한다.
 3) 문자나, _ 로 시작한다.
 4) 특수문자를 사용하면 안된다.
'''
a,b,c = 3,2,1

print(a,b,c)

#값 교환 - 프로그래밍에서 많이씀
a,b = 10, 20
print(a,b)
a,b = b,a
print(a,b)

#변수 타입
a = 123456782569871598715
print(a)
a=12.123456789123456789
print(a) # 8byte 용량까지만 출력이 됨
a = "student"
print(a)

#출력방식
print("number")
a,b,c = 1,2,3
print(a,b,c)
print("number : ", a,b,c)
print(a,b,c, sep=',')
print(a,b,c, sep='')
print(a,b,c, sep='\n')
print(a, end = ' ')
print(b, end = ' ')
print(c)





