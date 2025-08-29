# 강사님 코드

T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    players = list(map(int, input().split()))
    players.sort() # 오름차순 정렬

    left, right = 0, 0
    ret = 0

    while left < n and right < n:
        # 실력차이가 K 초과
        if players[right] - players[left] > k:
            left += 1 # 범위 좁히기
        else: # 실력차이가 K 이하
            right += 1 # 범위 넓히기

        # right-left+1
        # right가 +1 되고 크기를 계산
        # right-left
        ret = max(right-left, ret)
    print(f'#{tc} {ret}')
