T = int(input())

def rock_flip2():
    N, M = map(int, input().split())
    arr = list(map(int,input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        index = i - 1
        for k in range(1, j + 1):
            km = index - k
            kp = index + k
            if km < 0 or kp > len(arr) - 1: continue
            if arr[km] == arr[kp]:
                if arr[kp] == 0:
                    arr[kp] = 1
                    arr[km] = 1
                else:
                    arr[km] = 0
                    arr[kp] = 0
    return arr
            
for t in range(T):
    arr = rock_flip2()
    print(f'#{t + 1}', *arr)