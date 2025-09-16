def Find(n):
    if boss[n] == n: return n
    result = Find(boss[n]) # 재귀호출
    boss[n] = result # 경로압축
    return result

def Union(t1, t2):
    a = Find(t1)
    b = Find(t2)
    if a == b: return
    boss[b] = a

boss = [i for i in range(100)]
members = []
cnt = 0
sum_v = 0

n, node = map(int, input().split()) #n: 친구 관계, node:노드의 개수

# 구현 1번 : 비용을 기준으로 정렬
for _ in range(n):
    a, b, price = input().split()
    a, b = ord(a), ord(b)
    price = int(price)
    members.append((price, a, b)) # price를 첫번째 요소로
members.sort()

# 구현 2. 다른 그룹이면 그룹 맺기
for price, a, b in members:
    if Find(a) == Find(b): continue
    Union(a, b)
    cnt += 1
    sum_v += price

print(sum_v)