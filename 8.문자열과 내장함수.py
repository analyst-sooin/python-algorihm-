'''
문자열과 내장함수
'''
msg ="It is Time"
print(msg.upper())
print(msg.lower())
print(msg)
tmp = msg.upper()
print(tmp)
print(tmp.find('T')) #T라는 문자를 찾아서 index를 반환함
print(tmp.count('T')) # T라는 대문자가 몇개 있는지 반환함
print(msg)
print(msg[:2])
print(msg[3:5])
print(len(msg))
for i in range(len(msg)):
    print(msg[i], end =' ')
print()


for x in msg:
    print(x, end = ' ')
print()

for x in msg:
    if x.isupper():
        print(x, end = ' ')
print()

for x in msg:
    if x.islower():
        print(x, end = ' ')
print()
        
for x in msg:
    if x.isalpha():
        print(x, end = '')
print()

tmp ='AZ'
for x in tmp:
    print(ord(x))

tmp ='az'
for x in tmp:
    print(ord(x))

tmp = 65
print(chr(tmp))















