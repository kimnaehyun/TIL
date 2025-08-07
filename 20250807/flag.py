# flag 처리: flag 변수를 bool 타입 변수로 활용
# for - break -> break 를 함수의 return으로 변경
# Q.arr1과 arr2가 같은가?
arr1 = [1, 4, 2, 5]
arr2 = [1, 4, 3, 5]
flag = 0 # false로 초기화

for i in range(4):
    if arr1[i] != arr2[i]: # 하나라도 같지 않으면
        flag = 1
        break
if flag: print('x')
else: print('o')

def is_same():
    for i in range(4):
        if arr1[i] != arr2[i]:
            return 1 # 하나라도 같으면 return 1
    return 0 # 모두 같으면 return 0


result = is_same()
if result: print('o')
else: print('x')

