import heapq

MAP = [[0] * 6 for _ in range(6)]
MAP[0][1] = 15
MAP[0][2] = 17
MAP[0][3] = 22
MAP[1][2] = 5
MAP[2][3] = 6
MAP[2][4] = 2
MAP[2][5] = 8
MAP[3][5] = 7
MAP[4][5] = 1

def dijkstra(start):
    n = len(MAP) 
    result = [float('inf')] * n
    result[start] = 0 
    q = [(0, start)] 

    while q: 
        price, now = heapq.heappop(q) 

        if result[now] < price: continue 

        for i in range(n):
            if MAP[now][i] == 0: continue
            next_price = MAP[now][i] 
            price_sum = price + next_price 
            if result[i] > price_sum: 
                result[i] = price_sum
                heapq.heappush(q, (price_sum, i))

    return result

arr = dijkstra(0)
print(*arr)

'''
강사님 코드
import heapq

MAP =[[0] * 6 for _ in range(6)]

MAP[0][1] = 15
MAP[0][2] = 17
MAP[0][3] = 22
MAP[1][2] = 5
MAP[2][3] = 6
MAP[2][4] = 2
MAP[2][5] = 8
MAP[3][5] = 7
MAP[4][5] = 1

def dijkstra(start):
    n = len(MAP) # 노드수 6개
    result = [float('inf')] * n
    result[start] = 0 # 시작 노드
    q = [(0, start)] # 비용, 노드

    while q: # pq가 빌때까지 반복
        # 1. 힙에서 뺀다(탐색)
        price, now = heapq.heappop(q)

        if result[now] < price: continue # 더 큰 비용은 continue

        # 2 다음 갈 곳 예약 걸기(힙등록)
        for i in range(n):
            if MAP[now][i] == 0: continue
            next_price = MAP[now][i]
            price_sum = price + next_price # 비용 누적
            if result[i] > price_sum: # 더 적은 비용을 발견하면
                result[i] = price_sum # 갱신
                # 힙등록
                heapq.heappush(q, (price_sum, i))

    return result

result = dijkstra(0) # start는 0
print(*result)
'''