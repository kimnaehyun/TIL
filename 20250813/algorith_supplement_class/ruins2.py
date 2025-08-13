T = int(input())

def ruins2():
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    word_value = []
    
    for y in range(N):
        cnt = 0
        for x in range(M):
            if arr[y][x]: cnt += 1
            elif arr[y][x] == 0: 
                word_value.append(cnt)
                cnt = 0
        word_value.append(cnt)
        
    for y in range(N):
        cnt = 0
        for x in range(M):
            if arr[x][y]: cnt += 1
            elif arr[x][y] == 0: 
                word_value.append(cnt)
                cnt = 0
        word_value.append(cnt)
        
    return(max(word_value))


for tc in range(1, T + 1): print(f'#{tc}', ruins2())