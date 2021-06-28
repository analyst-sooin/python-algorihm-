
# 최솟값 구하기
arr = [5, 3, 7, 9, 2, 5, 2, 6]
# 가장작은 숫자가 저장될 변수 지정
arrMin = float('inf') # 파이썬에서 가장 큰값으로 저장하여 초기화

for i in range(len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]
print(arrMin)