boss = [i for i in range(10)]

def Find(n):
    if boss[n] == n: 
        return n 

    result = Find(boss[n])
    boss[n] = result 
    return result

def Union(t1, t2):
    a = Find(t1) 
    b = Find(t2) 
    if a == b: return
    boss[b] = a 

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    Union(x, y)

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    
    if Find(a) == Find(b): print('O')
    else: print('X')