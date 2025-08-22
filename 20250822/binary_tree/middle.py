bt = [0,9,4,12,3,6,0,15,0,0,0,0,0,0,13,17]
bt += [0] * 100

def dfs(now): 
    if bt[now] == 0: return
    
    dfs(now * 2)
    print(bt[now], end= ' ')
    dfs(now * 2 + 1)

dfs(1)