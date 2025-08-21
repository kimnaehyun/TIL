import heapq

n = int(input())
data = [(9, 'A'), (8, 'B'), (9, 'A'), (10, 'C'), (15, 'A')]
pq = []

# (숫자, -ord(문자)) # 숫자 최소힙, 문자 최대힙
# 최대힙이 push하기 전에 - 붙여서
for num, char in data:
    heapq.heappush(pq, (num, -ord(char)))

# n번반복
for _ in range(n):
    # 1. 가장 작은수 제거
    num, neg_ascii = heapq.heappop(pq)
    # 2. 계산 후 다시 삽입
    new_num = (num * 2) % 17
    heapq.heappush(pq, (new_num, neg_ascii))

while pq:
    num, neg_ascii = heapq.heappop(pq)
    # pop한 후에 -를 붙임
    print(f'({num}, {chr(-neg_ascii)})', end = ' ')
