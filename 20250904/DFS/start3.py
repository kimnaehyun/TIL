n = int(input())
MAP = [
    [0, 7, 20, 8],
    [0, 0, 5, 0],
    [15, 0, 0, 0],
    [0, 0, 6, 0]
]

used = [0] * 4
used[0] = 1 # 시작노드 방문처리

# 모든 경로를 탐색 (used배열을 지워줘야한다)
def dfs(now, sum_v):
    # 목적지에 도착하면
    if now == n: print(sum_v, end = ' ')

    for i in range(4):
        if MAP[now][i] == 0: continue
        if used[i] == 1: continue
        used[i] = 1
        # dfs(i, sum_v + 인접행렬의 좌표)
        dfs(i, sum_v + MAP[now][i])
        used[i] = 0 # 모든 경로 탐색
        
dfs(0, 0)