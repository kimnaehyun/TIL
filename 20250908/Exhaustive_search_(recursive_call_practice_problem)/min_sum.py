'''
dfs로 풀건데 그러면 dfs재귀호출을 언제할거냐??
좌표를 이동할때 dfs호출

1-1. 오른쪽으로 이동 할때 dfs호출 dfs(y, x, sum_v)
1-2. 아래로 이동 할때 dfs 호출 dfs(y, x, sum_v)

2. 정점 노드에 도달하면 return (좌표 끝 - 우측 하단)
    if y == N - 1 and x == N - 1:
    최소값 갱신(min_sum)
        return

3. 가지치기 (sum_v를 재귀호출 할때마다 갱신)
    sum_v >= min_sum -> 가지치기

'''
def dfs(y, x, sum_v):
    global min_sum

    # 좌표 끝에 도달 했을때(정점 노드에 도달 했을때)
    if y == N - 1 and x == N - 1:
        # 최소값 갱신하고 return
        min_sum = min(min_sum, sum_v)
        return

    # 가지치기
    if sum_v >= min_sum:
        return

    # 오른쪽으로 이동
    if x < N - 1:
        dfs(y, x + 1, sum_v + arr[y][x + 1])

    # 아래로 이동
    if y < N - 1:
        dfs(y + 1, x, sum_v + arr[y + 1][x])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = float('inf')
    dfs(0, 0, arr[0][0])
    print(f'#{tc} {min_sum}')
