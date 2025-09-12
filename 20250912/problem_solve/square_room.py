dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(y, x):
    global cnt
    # 4방향탐색
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        # 특정조건(1. 좌표범위내에 있어야한다. 2. 정확히 1이 큰값인 경우)
        if 0 <=ny <N and 0 <= nx < N and arr[ny][nx] == arr[y][x] + 1:
            cnt += 1
            dfs(ny, nx)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    min_start = float('inf')

    for y in range(N):
        for x in range(N):
            cnt = 1
            # dfs 호출하면서
            dfs(y, x)
            # max_cnt 갱신
            if cnt > max_cnt:
                max_cnt = cnt
                min_start = arr[y][x] # 최대값 갱신 됐을대 start 지점
            elif cnt == max_cnt: # min_start 갱신
                min_start = min(min_start, arr[y][x])

    print(f'#{tc} {min_start} {max_cnt}')