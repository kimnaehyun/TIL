arr = [[] for _ in range(4)]

arr[0] = [1, 3]
arr[1] = [2]
arr[2] = [0, 3]
arr[3] = [2]

visited = [0] * 4

def dfs(v):
    visited[v] = 1
    print(v)
    for nxt in arr[v]:
        if not visited[nxt]: dfs(nxt)

dfs(0)