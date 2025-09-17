import heapq

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dijkstra(MAP):
    result = [[float('inf')] * m for _ in range(n)]
    result[0][0] = MAP[0][0] # 시작 위치
    q = [(MAP[0][0], 0, 0)] # 비용, 노드

    while q:
        # 1. 힙에서 뺀다
        cost, y, x = heapq.heappop(q)

        # 이미 처리된 비용보더 더 큰 비용이 발생하면 continue
        if result[y][x] < cost: continue

        # 2. 다음 갈곳 예약 걸기(힙등록)
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m: continue # 범위체크
            next_price = result[y][x] + MAP[ny][nx]
            if result[ny][nx] > next_price: # 최소 비용 갱신
                result[ny][nx] = next_price
                # 힙등록
                heapq.heappush(q, (next_price, ny, nx))

    return result[n-1][m-1]

n, m = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]
print(dijkstra(MAP))