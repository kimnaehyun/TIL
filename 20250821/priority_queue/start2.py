import heapq

arr = [(7, 'A'), (9, 'C'), (7, 'C'), (6, 'D'), (5, 'A')]
arr2 = [(i[1], -i[0]) for i in arr]
arr3 = []

while arr2: heapq.heappush(arr3, heapq.heappop(arr2))
for i in arr3: print(f'({-i[1]}, {i[0]})', end= ' ')