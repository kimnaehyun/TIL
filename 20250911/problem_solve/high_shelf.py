T = int(input())

def sum_value():
    value = 0
    global min_value
    for i in range(len(path)):
        if path[i] : value += num_arr[i]
    if value >= B:
        if min_value > value - B :
            min_value = value - B 

def dfs(lev):
    if lev == N:
        sum_value()
        return
    for i in range(2):
        path.append(tf_arr[i])
        dfs(lev + 1)
        path.pop()

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    num_arr = list(map(int, input().split()))
    path = []
    tf_arr = [1, 0]
    min_value = float('inf')
    dfs(0)
    print(f'#{tc} {min_value}')