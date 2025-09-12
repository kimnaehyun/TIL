dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(y, x, sum_v):
    # 길이가 7이면 return (기저조건)
    if len(sum_v) == 7:
        result.add(sum_v) # 세트(중복제거)
        return

    for i in range(4): # 4방향
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 > ny or 0 > nx or ny >= 4 or nx >= 4: continue
        dfs(ny, nx, sum_v + arr[ny][nx])

T = int(input())
for tc in range(1, T + 1):
    arr = [input().split() for _ in range(4)]
    result = set()
    # 시작지점 - 임의의 좌표
    for y in range(4):
        for x in range(4):
            dfs(y, x, arr[y][x])
    print(f'#{tc} {len(result)}')