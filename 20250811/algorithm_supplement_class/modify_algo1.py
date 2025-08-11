T = int(input())

def scouter():
    N, M, K = map(int, input().split())
    arr = [input() for _ in range(N)]

    for y in range(N - M + 1):
        for x in range(N - M + 1):
            count = 0
            for i in range(y, y + M):
                for j in range(x, x + M):
                    if arr[i][j] == '*':
                        count += 1
            if count == K:
                return y, x
    return -1, -1  



for t in range(T):
    y, x = scouter()
    print(f'#{t + 1} {y} {x}')