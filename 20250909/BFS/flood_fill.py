from collections import deque

visited = [[0] * 5 for _ in range(5)]

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

def flood_fill(start_y, start_x):
    q = deque()
    q.append((start_y, start_x))
    visited[start_y][start_x] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= 5 or nx < 0 or nx >= 5: continue
            if visited[ny][nx]: continue
            q.append((ny, nx))
            visited[ny][nx] = visited[y][x] + 1


start_y, start_x = map(int, input().split())
flood_fill(start_y, start_x)
for i in visited: print(*i)

'''
강사님 코드
# 플러드필
# bfs + 좌표(방향배열)
from collections import deque

# 5x5 행렬
visited = [[0] * 5 for _ in range(5)]

# 방향 배열
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def flood_fill(start_y, start_x):
    q = deque()
    q.append((start_y, start_x)) # 시작 좌표를 큐에 추가
    visited[start_y][start_x] = 1 # 시작 좌표를 방문 처리

    while q:
        # 1. 큐에서 뺀다(탐색)
        now_y, now_x = q.popleft()
        # 2. 다음 갈곳 예약 걸기
        for i in range(4): # 4방향
            ny = now_y + dy[i]
            nx = now_x + dx[i]

            # 방향배열 범위체크 (좌표 범위체크)
            if ny < 0 or nx < 0 or ny >= 5 or nx >= 5: continue

            # 이미 방문했으면 continue
            if visited[ny][nx] != 0: continue

            # 큐 등록 + 거리 업데이트
            visited[ny][nx] = visited[now_y][now_x] + 1
            q.append((ny, nx))


# 함수 호출
sty, stx = map(int, input().split())
flood_fill(sty, stx)

# 결과 출력
for y in range(5):
    for x in range(5):
        print(visited[y][x], end = " ")
    print()
'''