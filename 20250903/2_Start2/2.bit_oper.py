print(1 << 1, bin(1 << 1))
print(1 << 4, bin(1 << 4))
print(7 >> 1, bin(7 >> 1))

num = 2
for _ in range(5):
    print(num, end = ' ')
    num = num << 1
print()

# 1. 부분집합의 수를 바로 구할 수 있다.
arr = [1, 2, 3, 4]
print(f'부분 집합의 수: {1 << len(arr)}')

# 2. 전체 부분 집합을 구할 수 있다.
for i in range(1 << len(arr)): # 부분집합 번호
    for idx in range(len(arr)): # 각 원소들을 모두 확인
        # i: 부분집합 번호(각 자리의 포함 여부)
        # (1 << idx): 0b1, 0b10, 0b100, 0b1000
        if i & (1 << idx): print(arr[idx], end = ' ')
    print()

# 3. 응용. 합이 10인 부분 집합만 구해라.
arr3 = [1, 2, 3, 4, 5, 6]
for i in range(1 << len(arr3)):
    subset = []
    total = 0 

    for idx in range(len(arr3)): 
        if i & (1 << idx):
            subset.append(arr3[idx])
            total += arr3[idx]

    if total == 10: print(f'합이 10인 부분집합: {subset}')
