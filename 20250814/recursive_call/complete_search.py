path = []
cnt = 0
n = int(input())

def KFC(lev, sum_v): # 재귀호출 될 때마다 합계가 누적
    # cnt = 0 # 재귀호출 할때마다 0으로 초기화
    global cnt

    # 가지치기
    if sum_v > 10: return

    if lev == n:
        # if sum_v <= 10: cnt += 1 # 비효율적(모든 경우를 다 탐색해서 느리다)
        cnt += 1
        return

    for i in range(1, 7): # branch : 6
        path.append(i)
        KFC(lev + 1, sum_v + i)
        path.pop()

KFC(0, 0) # level, sum_v
print(cnt)