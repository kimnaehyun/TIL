import heapq

heap = []
values = [5, 2, 8, 1, 9]
heap_sort = []

for value in values: heapq.heappush(heap, -value)
while heap: heap_sort.append(heapq.heappop(heap))

print(list(map(abs ,heap_sort)))