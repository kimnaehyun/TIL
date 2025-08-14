n = int(input())
path = []
used = [0] * 7

def KFC(lev):
    
    if lev == n: 
        print(*path)
        return

    for i in range(1, 7):
        if used[i] == 1: continue
        used[i] = 1
        path.append(i)
        KFC(lev + 1)
        path.pop()
        used[i] = 0 

KFC(0)