import heapq

pq = []
heapq.heappush(pq, 5)
heapq.heappush(pq, 2)
heapq.heappush(pq, 8)
heapq.heappush(pq, 1)
heapq.heappush(pq, 9)
heapq.heappush(pq, 4)

sorted_arr = []

while pq: # pq가 빌때까지 반복 -> heap sort
    sorted_arr.append(heapq.heappop(pq))

print(sorted_arr) 

for i in sorted_arr:
    pass 