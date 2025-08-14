# 11111111111 ~ 666666666666 -> 10중 for문?

path = []

def KFC(lev):
    if lev == 3: # 주사위 3개 던진다.
        print(*path)
        return
    
    for i in range(1, 7): # 주사위 눈금이 1~6까지 (branch 6)
        path.append(i)
        KFC(lev + 1)
        path.pop()

KFC(0)