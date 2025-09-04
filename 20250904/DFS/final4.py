arr = [
    [0, 2, 6, 3, 0, 0],
    [2, 0, 7, 4, 0, 0],
    [6, 7, 0, 0, 0, 0],
    [3, 4, 2, 0, 0, 0],
    [0, 0, 1, 0, 0, 7],
    [0, 0, 0, 0, 0, 0]
]

N = len(arr)
visited = [0] * N
a, b = map(int, input().split())
result = []
def dfs(start, cost):
    global result
    if start == b:
        result.append(cost)
        return cost
    for v in range(6):
        if arr[start][v] != 0 and not visited[v]:
            visited[start] = 1
            dfs(v, cost + arr[start][v])
            visited[start] = 0
dfs(a, 0)
min_v = min(result)
max_v = max(result)
print(max_v)
print(min_v)