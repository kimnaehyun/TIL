T = int(input())

def where_can_words_fit():
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    word_value = []
    
    for y in range(N):
        cnt = 0
        for x in range(N):
            if arr[y][x]: cnt += 1
            elif arr[y][x] == 0: 
                word_value.append(cnt)
                cnt = 0
        word_value.append(cnt)
        
    for y in range(N):
        cnt = 0
        for x in range(N):
            if arr[x][y]: cnt += 1
            elif arr[x][y] == 0: 
                word_value.append(cnt)
                cnt = 0
        word_value.append(cnt)
        
    return(word_value.count(K))


for tc in range(1, T + 1): print(f'#{tc}', where_can_words_fit())