from collections import deque

name = 'ACBQTPR'

MAP = [[0] * 7 for _ in range(7)] # 7x7 행렬
MAP[0][1] = 1
MAP[0][2] = 1
MAP[0][3] = 1
MAP[2][4] = 1
MAP[3][5] = 1
MAP[3][6] = 1

q = deque()
q.append(0) # 시작 노드 처리 (큐에 넣고 시작)

while q:
    # 1. 뺀다 (탐색)
    now = q[0]
    q.popleft()
    print(name[now], end = ' ')
    # 2. 예약걸기 (등록)
    for i in range(7):
        if MAP[now][i] == 0: continue
        q.append(i)