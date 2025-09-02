map = [[0] * 4 for _ in range(4)]

map[1][0] = 1
map[2][0] = 1
map[3][0] = 1
map[2][1] = 1
map[3][1] = 1

name = 'BTAR'

def DFS(n):
    for i in range(4):
        if map[n][i] : print(name[i])


DFS(int(input()))