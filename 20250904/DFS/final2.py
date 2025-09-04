MAP = [
    [0, 2, 6, 3, 0, 0],
    [2, 0, 7, 4, 0, 0],
    [6, 7, 0, 0, 0, 0],
    [3, 4, 2, 0, 0, 0],
    [0, 0, 1, 0, 0, 7],
    [0, 0, 0, 0, 0, 0],
]

used = [0] * 6

def dfs(now):
    print(now, end = ' ')
    for i in range(6):
        if MAP[now][i] == 0: continue
        if used[i] == 1: continue
        # 모든 노드 1회씩 방문
        used[i] = 1 # 방문기록
        dfs(i)
        used[i] = 0 # 모든 경로 : 노드를 다시 방문해야 하니까 (백트래킹)

dfs(4)
