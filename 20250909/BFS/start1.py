from collections import deque

alist = [[] for _ in range(5)]

alist[0] = [1, 2]
alist[1] = [2]
alist[2] = [3]
alist[3] = [4]

q = deque()
q.append(0) 
name = 'ABCDE'
used = [0] * 5
used[0] = 1   

while q:
    now = q.popleft()
    print(name[now], end=' ')

    for next in alist[now]:
        if not used[next]:   
            q.append(next)
            used[next] = 1

'''
강사님 코드
from collections import deque

def bfs(start):
    q = deque()
    used = [0] * 6
    # 큐에 start 노드 넣고, 시작노드 방문처리
    q.append(start)
    used[start] = 1

    while q:
        # 1. 큐에서 뺀다 (탐색)
        now = q[0]
        print(chr(now + ord('A')), end = ' ')
        q.popleft()
        # 2. 다음 갈곳 예약 걸기(큐 등록)
        for i in range(len(alist[now])):
            next = alist[now][i]
            # 이미 탐색했으면 continue
            if used[next] == 1: continue
            # 방문 표시
            used[next] = 1
            q.append(next) # 예약 걸기
            # 방문기록 지우지 X



alist = [[] for _ in range(6)]
alist[0] = [1, 2]
alist[1] = [0, 2]
alist[2] = [0, 1, 3]
alist[3] = [2, 4]
alist[4] = [3]
n = int(input())
bfs(n)
'''