pipe = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 0, 1 ], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0]]

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

opp = [1, 0, 3, 2]

def fugitive_arrest():
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    