from heapq import heappop, heappush 

N, M, K = map(int, input().split())
A, B = map(int, input().split())

MAP = [[0] * N for _ in range(M)]

for _ in range(M):
    f, t, c = map(int, input().split())
    MAP[f][t] = c

def dijkstra(start):
    result = [float('inf')] * N
    result[start] = 0
    q = [(0, start)]

    while q:
        price, now = heappop(q)

        if result[now] < price: continue

        for i in range(M):
            if MAP[now][i] == 0: continue
            next_price = MAP[now][i]
            price_sum = price + next_price
            if result[i] > price_sum:
                result[i] = price_sum
                heappush(q, (price_sum, i))

    return result

arr = dijkstra(A)
print(arr[B])

y1 = int(input())

for i in range(len(MAP)):
    for j in range(len(MAP)):
        if MAP[i][j]: MAP[i][j] += y1

arr = dijkstra(A)
print(arr[B])

y2 = int(input())

for i in range(len(MAP)):
    for j in range(len(MAP)):
        if MAP[i][j]: MAP[i][j] += y2

arr = dijkstra(A)
print(arr[B])