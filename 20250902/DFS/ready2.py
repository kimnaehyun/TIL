map = [[0] * 5 for _ in range(5)]

map[0][1] = 1
map[1][2] = 1
map[1][3] = 1
map[2][1] = 1
map[4][1] = 1

arr = [1,2,3,4,5]

def DFS(n):
    index = arr.index(n)
    for i in range(5):
        if map[index][i] : print(arr[i])

DFS(int(input()))

# 강사님 코드
# MAP = [
#     [0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 0],
#     [0, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0]
# ]
# num = int(input()) # 노드 값
# n = num - 1 # 노드 번호
# for i in range(5):
#     if MAP[n][i] == 0: continue
#     print(i + 1) # 노드 값

# 정승현 코드
# arr = [(1, [1]), (2, [2, 3]), (3, [1]), (4, [-1]), (5, [1])]
# N = int(input())
# for i in range(len(arr)):
#     if arr[i][0] == N:
#         for j in range(len(arr[i][1])):
#             print(arr[arr[i][1][j]][0])