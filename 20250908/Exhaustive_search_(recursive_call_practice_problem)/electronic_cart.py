'''
1. branch, level : N-1

2. 음수인덱스
마지막 구역에서 사무실로 돌아오는 비용
arr[path[-1]][0]

3. 마지막 방문 지점의 이전에 방문한 지점
arr[path[-2]][i]
'''
def dfs(lev, sum_v):
    global min_v

    if lev == N - 1: # lev은 N-1
        # 마지막 구역에서 사무실로 돌아오는 비용
        sum_v += arr[path[-1]][0] #
        min_v = min(min_v, sum_v) # 최소값 갱신
        return

    for i in range(1, N): # branch N-1
        if used[i] == 1: continue
        used[i] = 1
        path.append(i)
        dfs(lev + 1, sum_v + arr[path[-2]][i])
        path.pop()
        used[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    path = [0] # 사무실 (0)에서 시작
    used = [0] * N
    used[0] = 1 # 사무실 방문처리
    min_v = float('inf')
    dfs(0, 0)
    print(f'#{tc} {min_v}')