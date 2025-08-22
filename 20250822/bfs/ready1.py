from collections import deque

alist = list([] for _ in range(7))

alist[5] = [3, 1] # 2번 반복 alist[now][i]
alist[3] = [2] # 1번 반복 alist[now][i]
alist[1] = [4]
alist[4] = [0, 6]

q = deque()
q.append(5) # start 지점

while q:
    # 1. 큐에서 뺀다 (탐색)
    now = q[0]
    q.popleft()
    print(now, end = ' ')

    # 2. 다음 갈곳 예약 걸기(큐 등록)
    for i in range(len(alist[now])):
        next = alist[now][i]
        q.append(next)