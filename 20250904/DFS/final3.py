MAP = [
    [0, 2, 6, 3, 0, 0],
    [2, 0, 7, 4, 0, 0],
    [6, 7, 0, 0, 0, 0],
    [3, 4, 2, 0, 0, 0],
    [0, 0, 1, 0, 0, 7],
    [0, 0, 0, 0, 0, 0],
]
used = [0] * 6
cnt = 0
a, b = map(int, input().split())

def dfs(now):
    global cnt
    if now == b: 
        cnt += 1
        return
        
    for i in range(6):
        if MAP[now][i] == 0: continue
        if used[i] == 1: continue
        used[i] = 1 
        dfs(i)
        used[i] = 0


dfs(a)
print(cnt)