import heapq

arr = [5, 2, 8, 1, 9, 4]
pq = []

sorted_arr = []

while arr: 
    heapq_heappop = heapq.heappop(arr)
    heapq.heappush(pq, (heapq_heappop % 2, heapq_heappop))

while pq: heapq.heappush(sorted_arr,heapq.heappop(pq))
for i in sorted_arr: print(i[1], end=' ')
