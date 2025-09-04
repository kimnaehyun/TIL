MAP = [[0] * 4 for _ in range(4)]
MAP[0][1] = 1
MAP[0][3] = 1
MAP[1][2] = 1
MAP[2][0] = 1
MAP[2][3] = 1
MAP[3][2] = 1

used = [0] * 4
def m_dfs(now):
    print(now)
    
    for i in range(4):
        if MAP[now][i] == 0: continue
        if used[i]: continue
        used[i] = 1
        m_dfs(i)

m_dfs(0)

arr = [[] for _ in range(4)]

arr[0] = [1, 3]
arr[1] = [2]
arr[2] = [0, 3]
arr[3] = [2]

visited = [0] * 4

def v_dfs(now):
    print(now)
    visited[now] = 1
    for nxt in arr[now]:
        if not visited[nxt]: v_dfs(nxt)

v_dfs(0)



'''
# 강사님 코드

# 그래프의 dfs 인접행렬
MAP = [[0] * 4 for _ in range(4)]

MAP[0][1] = 1
MAP[0][3] = 1
MAP[1][2] = 1
MAP[2][0] = 1
MAP[2][3] = 1
MAP[3][2] = 1

used = [0] * 4
used[0] = 1 # 시작노드 방문 처리

def dfs(now):
    print(now)
    for i in range(4):
        if MAP[now][i] == 0: continue
        # 이미 갔던 곳(방문했던 곳)이라면 무시
        if used[i] == 1: continue
        # 방문표시
        used[i] = 1
        dfs(i)

dfs(0)

# 그래프의 dfs 인접 리스트
m = [[] for _ in range(4)]
m[0] = [1, 3]
m[1] = [2]
m[2] = [0, 3]
m[3] = [2]

used = [0] * 4
used[0] = 1 # 시작노드 방문표시

def dfs(now):
    print(now)
    for i in range(len(m[now])):
        next = m[now][i]
        # used 검사( 한번 갔던 곳은 안가겠다.)
        if used[next] == 1: continue
        # 방문했으면 방문했다고 기록
        used[next] = 1
        dfs(next)

dfs(0)

'''