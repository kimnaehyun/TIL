# 3행 2차원 빈배열
m = [[] for _ in range(3)]

m[0] = ['A', 'B', 'T']
m[2] = ['R', 'S']

for y in range(len(m)): # 3번
    # 거꾸로 순회
    for x in range(len(m[y]) - 1, -1, -1): # 3번, 0번, 2번
        print(m[y][x], end = '')
    print() # 줄바꿈