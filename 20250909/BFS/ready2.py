from collections import deque

n = 7
matrix = [[0] * n for _ in range(n)]

matrix[0][1] = 1
matrix[0][2] = 1
matrix[0][3] = 1
matrix[2][4] = 1
matrix[3][5] = 1
matrix[3][6] = 1

name = 'ACBQTPR'

q = deque()
visited = [False] * n  

q.append(0)
visited[0] = True

while q:
    now = q.popleft() 
    print(name[now], end=' ')

    for i in range(n):
        if matrix[now][i] == 1 and not visited[i]:
            q.append(i)
            visited[i] = True
