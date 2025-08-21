'''
n = int(input())
scores = [500] # 초기값 500

for _ in range(n): # N
    a, b = map(int, input().split())
    scores.append(a)
    scores.append(b)
    scores.sort() # NlogN

    length = len(scores)
    mid = scores[length // 2]

    print(mid)

# 시간복잡도 O(N제곱 logN)
'''

import heapq

max_heap = [] # 내림차순 중간값 보다 작은값 (최대힙)
min_heap = [] # 오름차순 중간값 보다 큰값 (최소힙)
mid = 500

def push(v):
    if mid > v: # 중간값 보다 작으면 최대 힙에 추가
        heapq.heappush(max_heap, -v)
    else: # 중간값보다 크거나 같으면 최소 힙에 추가
        heapq.heappush(min_heap, v)

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    push(a)
    push(b)

    # 경우가 두가지 1. 왼쪽이 더 많을 경우 (최대힙의 크기가 더 클경우)
    # 2. 오른쪽이 더 많을 경우 (최소힙의 크기가 더 클경우)

    if len(max_heap) > len(min_heap):
        # 최대힙이 많으니까 최소힙에 넣기 (갯수맞추기)
        heapq.heappush(min_heap, mid)
        # 최대 힙에서 가장 큰값 꺼내서 새로운 중간값으로 설정
        mid = -heapq.heappop(max_heap)
    elif len(max_heap) < len(min_heap):
        heapq.heappush(max_heap, -mid)
        mid = heapq.heappop(min_heap)

    print(mid)

# 시간복잡도가 NlogN

