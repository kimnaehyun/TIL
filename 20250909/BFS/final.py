from collections import deque

n = 5
matrix = [[0] * 5 for _ in range(n)]

matrix[0][1] = 1
matrix[0][4] = 1
matrix[1][3] = 1
matrix[1][4] = 1
matrix[2][0] = 1
matrix[3][0] = 1
matrix[3][2] = 1


def BFS():
    q = deque()
    min_value = float('inf')
    count = 0
    start, end = map(int, input().split())
    q.append(start)

    while q:
        now = q.popleft() 
        count += 1
        for i in range(n):
            
            if matrix[now][i] == 1 and i == end :
                if min_value > count:
                    min_value = count 
                break
            if matrix[now][i] == 1: q.append(i)
    return min_value

print(BFS())

'''
강사님 코드
from collections import deque

MAP = [
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

q = deque()
used = [0] * 5
start, end = map(int, input().split())
# start 노드 q에 넣어주고,
# level도 같이 넣어준다. q.append((node, level))
q.append((start, 0))
used[start] = 1 # 시작노드 방문처리

while q:
    # 1. 큐에서 뺀다(탐색)
    now, level = q[0]
    q.popleft()

    # now가 end에 도착했을때 break
    if now == end:
        print(level) # 비행기를 몇번 탔는지
        break

    # 2. 다음 갈곳 예약 걸기(큐에 등록)
    for i in range(5):
        if MAP[now][i] == 0: continue
        if used[i] == 1: continue
        used[i] = 1
        q.append((i, level + 1)) # 큐 등록
'''