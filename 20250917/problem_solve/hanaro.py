'''
하나로 (크루스칼 알고리즘) 전략
def Find(n):
    if boss[n] == n: return n # 자기자신이라면 boss
    result = Find(boss[n]) # 재귀호출
    boss[n] = result # 경로압축
    return result

def Union(t1, t2):
    # t2의 보스가 t1의 보스 밑으로 들어간다
    a = Find(t1)
    b = Find(t2)
    if a == b: return # 이미 같은 그룹이면 탈락
    boss[b] = a
    
# 구현 1. 비용을 기준으로 오름차순 정렬
# 구현 2. 다른그룹이면 그룹맺기
# 두 섬 사이의 거리 계산
dist = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
cost = E * dist 
'''
def Find(n):
    if boss[n] == n: return n

    boss[n] = Find(boss[n]) 
    return boss[n]

def Union(t1, t2):
    a = Find(t1)
    b = Find(t2)

    if a == b: return False

    boss[b] = a

    return True

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    tax = float(input())
    edges = []

    for i in range(N):
        for j in range(i + 1, N):
            cost = ((x_list[i] - x_list[j]) ** 2 + (y_list[i] - y_list[j]) ** 2) * tax
            edges.append((cost, i, j))
    
    edges.sort()

    boss = [i for i in range(N)]
    cnt = 0
    min_cost = 0

    for w, u, v in edges:
        if Union(u, v):
            min_cost += w
            cnt += 1
        if cnt == N - 1: break

    print(f'#{tc} {min_cost:.0f}')


'''
def Find(n):
    if boss[n] == n: return n # 자기자신이라면 boss
    result = Find(boss[n]) # 재귀호출
    boss[n] = result # 경로압축
    return result

def Union(t1, t2):
    # t2의 보스가 t1의 보스 밑으로 들어간다
    a = Find(t1)
    b = Find(t2)
    if a == b: return # 이미 같은 그룹이면 탈락
    boss[b] = a

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input()) # 환경 부담 세율

    boss = [i for i in range(N)]
    members = []
    cnt = 0 # 선택된 간선의 개수
    sum_v = 0 # 총 환경 부담금

    # 구현 1. 비용을 기준으로 오름차순 정렬
    for i in range(N):
        for j in range(i + 1, N):
            dist = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
            cost = E * dist
            members.append((cost, i, j))
    members.sort()
    # 구현 2. 다른그룹이면 그룹맺기
    for cost, a, b in members:
        if Find(a) == Find(b): continue
        Union(a, b)
        cnt += 1
        sum_v += cost

    print(f'#{tc} {round(sum_v)}')
'''