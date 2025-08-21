# 미로1 문제 코드

```python
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]



def bfs(start_y, start_x):
    q = [(start_y, start_x)]

    # 후보군이 없을 때 까지 반복
    while q:
        now_y, now_x = q.pop(0)

        # now_y, now_x 로부터 상하좌우를 확인
        for i in range(4):
            new_y = now_y + dy[i]
            new_x = now_x + dx[i]

            # 범위 밖으로 나가는 경우를 제외(continue)
            if new_y < 0 or new_y >= 16 or new_x < 0 or new_x >= 16:
                continue

            # 벽이라면 제외(continue)
            if matrix[new_y][new_x] == 1:
                continue

            # 도착하면 return 1
            if matrix[new_y][new_x] == 3:
                return 1

            # 이미 방문한 좌표는 패스(continue)
            if visited[new_y][new_x]:
                continue

            visited[new_y][new_x] = 1  # 방문 기록
            q.append((new_y, new_x))

    # 도달 못하면 0 return
    return 0


for _ in range(10):
    tc = int(input())
    matrix = [list(map(int, input())) for _ in range(16)]

    # 처음 좌표 기록
    start_y, start_x = 0, 0
    for i in range(16):
        for j in range(16):
            if matrix[i][j] == 2:
                start_y, start_x = i, j

    # 특정 좌표에 방문 했는 지 여부를 기록
    # - 16*16 0배열
    # visited = [[0] * 16] * 16  # 얕은복사
    visited = [[0] * 16 for _ in range(16)]
    visited[start_y][start_x] = 1  # 출발점은 방문했다고 가정하고 시작

    result = bfs(start_y, start_x)
    print(f'#{tc} {result}')
```
