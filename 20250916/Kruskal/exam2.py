'''
힌트
1. 비용 기준으로 오름차순 정렬

2. 다른 그룹이면 그룹맺기
   + 다른 성별이면 그룹맺기

3. 모든 노드가 연결되어 있는지 확인
   (간선의 개수 == 노드의 개수 - 1)
   cnt == N - 1: 
'''
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

N, M = map(int, input().split())
boss = [i for i in range(N + 1)]
gender_input = input().split()
# 노드가 1번부터
gender = [0] + gender_input

# 전략 1번 : 비용을 기준으로 오름차순 정렬
edges = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))
# 비용 기준으로 정렬(람다함수)
edges.sort(key=lambda x : x[2])

sum_cost = 0
cnt = 0

# 전략 2. 다른그룹이면 그룹맺기, 다른 성별이면 그룹맺기
for a, b, cost in edges:
    if Find(a) == Find(b): continue
    if gender[a] == gender[b]: continue
    cnt += 1
    sum_cost += cost
    Union(a, b)

if cnt == N - 1: print(sum_cost)
else: print(-1)