boss = [i for i in range(200)]

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
    a, b = input().split()
    Union(ord(a), ord(b))


a, b = input().split()
if Find(ord(a)) == Find(ord(b)): print('O')
else: print('X')
