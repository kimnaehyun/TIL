from heapq import heappop, heappush 

MAP = [[0] * 200 for _ in range(200)]
a = ord("A")
b = ord("B")
c = ord("C")
d = ord("D")
e = ord("E")
f = ord("F")
MAP[a][b] = 5
MAP[a][c] = 10
MAP[a][d] = 7
MAP[a][f] = 12
MAP[b][a] = 5
MAP[b][f] = 9
MAP[c][f] = 1
MAP[d][c] = 2
MAP[d][e] = 1
MAP[e][f] = 3

def dijkstra(start):
    n = len(MAP)
    result = [float("inf")] * n
    result[start] = 0
    q = [(0, start)]

    while q:
        price, now = heappop(q)

        if result[now] < price: continue

        for i in range(n):
            if MAP[now][i] == 0: continue
            next_price = MAP[now][i]
            price_sum = price + next_price
            if result[i] > price_sum:
                result[i] = price_sum
                heappush(q, (price_sum, i))
    
    return result

s, e = input().split()

arr = dijkstra(ord(s))
print(arr[ord(e)])
