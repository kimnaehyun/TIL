import heapq

data = [(2, 'BHC'), (1, 'NeNe'), (3, 'KFC'), (1, 'BBQ'), (2, 'Moms'), (4, 'MC')]
pq = []

# 크기 순으로 정렬되도록
for size, name in data:
    heapq.heappush(pq, (size, name))

# 한마리 남을때 까지 병함
while len(pq) > 1:
    # 가장 작은 미생물 두마리 꺼내기(최소힙)
    size1, name1 = heapq.heappop(pq)
    size2, name2 = heapq.heappop(pq)
    # 새로운 미생물생성
    new_size = size1 + size2
    # 사전순으로 앞에 있는 이름 선택
    new_name = min(name1, name2)
    # 새로 생성된 미생물 힙에 push
    heapq.heappush(pq, (new_size, new_name))
    
# 마지막 남은 미생물
final_size, final_name = heapq.heappop(pq)
print(final_name, final_size)