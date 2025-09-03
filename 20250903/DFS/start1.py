map = [[0] * 6 for _ in range(6)]

map[0][1] = 1
map[0][2] = 1
map[0][3] = 1
map[1][4] = 1
map[1][5] = 1

visited = [0] * 6

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(6):
        if map[v][i] == 1 and not visited[i]: dfs(i)

dfs(0)