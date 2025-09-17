import heapq

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dijkstra(MAP):
    result = [[float('inf')] * n for _ in range(n)]
    result[0][0] = int(MAP[0][0])
    q = [(int(MAP[0][0]), 0, 0)]

    while q:
        cost, y, x = heapq.heappop(q)

        if result[y][x] < cost: continue

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n: continue 
            next_price = result[y][x] + int(MAP[ny][nx])
            if result[ny][nx] > next_price: 
                result[ny][nx] = next_price
                heapq.heappush(q, (next_price, ny, nx))

    return result[n-1][n-1]

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    MAP = [list(input()) for _ in range(n)]
    print(f'#{tc} {dijkstra(MAP)}')

'''
강사님 코드
import heapq

def dijkstra(start):
    n = len(MAP)
    result = [[float('inf')] * n for _ in range(n)]
    result[0][0] = 0 # 시작 노드 초기화
    q = [(0, start)] # 비용, 노드

    while q:
        # 1. 힙에서 뺀다(탐색)
        price, now = heapq.heappop(q)
        # now는 현재 좌표(튜플형태)
        y, x = now

        if result[y][x] < price: continue

        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]

        # 다음갈곳 예약걸기(힙등록)
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n: continue
            next_price = MAP[ny][nx]
            price_sum = price + next_price
            if result[ny][nx] > price_sum: # 더 적은 비용이 나왔으면
                result[ny][nx] = price_sum # 최소비용 갱신
                # 힙등록
                heapq.heappush(q, (price_sum, (ny, nx)))
    return result

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input())) for _ in range(N)]
    start = (0, 0)
    result = dijkstra(start)
    print(f'#{tc} {result[N-1][N-1]}')
'''