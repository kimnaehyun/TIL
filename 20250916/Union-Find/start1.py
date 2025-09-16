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
    a, b = map(int, input().split())
    # 그룹맺기
    Union(a, b)

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    # 보스가 같으면 같은 그룹
    if Find(a) == Find(b): print('O')
    else: print('X')