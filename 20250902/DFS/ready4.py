arr = []
arr1 = [4, 2, 5, 1, 1]
arr2 = [3, 4, 2]
arr3 = []
arr4 = [1, 1, 2, 3]

arr += [arr1[:]]
arr += [arr2[:]]
arr += [arr3[:]]
arr += [arr4[:]]

for i in arr : print(i)

# 강사님 코드
m = [[] for _ in range(4)] # 4행 2차원 배열
m[0] = [4, 2, 5, 1, 1]
m[1] = [3, 4, 2]
m[3] = [1, 1, 2, 3]

for i in m:
    print(i)