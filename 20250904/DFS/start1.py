name = "ABTQVX"

MAP = [[0] * 6 for _ in range(6)]
MAP[0][1] = 1
MAP[0][2] = 1
MAP[0][3] = 1
MAP[1][4] = 1
MAP[1][5] = 1

def dfs(now):
    print(now, end = ' ')
    for i in range(6):
        if MAP[now][i] == 0: continue
        dfs(i)

dfs(0)