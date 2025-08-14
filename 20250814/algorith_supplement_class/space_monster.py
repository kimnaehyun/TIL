# T = int(input())

def space_monster():
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    cnt = 0
    
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 2:
                for i in range(4):
                    for j in range(1, N):
                        ny = y + dy[i] * j
                        nx = x + dx[i] * j
                        if ny < 0 or ny >= N or nx < 0 or nx >= N: continue
                        if arr[ny][nx] == 0: arr[ny][nx] = 2
                        else: break
    
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 0: cnt += 1
            
    return arr, cnt

print(space_monster())