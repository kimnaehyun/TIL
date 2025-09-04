MAP = [[0] * 5 for _ in range(5)]

MAP[0][1] = 1
MAP[0][3] = 1
MAP[0][4] = 1
MAP[1][2] = 1
MAP[1][3] = 1
MAP[3][2] = 1
MAP[3][4] = 1
MAP[4][1] = 1
MAP[4][3] = 1

alist = [[] for _ in range(5)]

alist[0] = [1, 3, 4]
alist[1] = [2, 3]
alist[3] = [2, 4]
alist[4] = [1, 3]

s = 'DUSRK'
n = int(input())
for i in range(len(MAP)):
    if MAP[n][i]: print(s[i])

for i in alist[n]: print(s[i])


'''
# 강사님 코드
# 인접행렬
MAP = [[0] * 5 for _ in range(5)] # 5x5 행렬
MAP[0][1] = 1
MAP[0][3] = 1
MAP[0][4] = 1
MAP[1][2] = 1
MAP[1][3] = 1
MAP[3][2] = 1
MAP[3][4] = 1
MAP[4][1] = 1
MAP[4][3] = 1
# 인접리스트
alist = [[] for _ in range(5)]
alist[0] = [1, 3, 4]
alist[1] = [2, 3]
alist[3] = [2, 4]
alist[4] = [1, 3]


node_name = 'DUSRK'

num = int(input())

for i in range(len(alist[num])):
    # 인접 행렬
    # if MAP[name][i] == 1: print()
    # 인접 리스트
    next = alist[num][i]
    print(node_name[next])

'''