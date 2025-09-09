T = int(input())

def increasing_candy_sequence():
    A, B, C = map(int, input().split())
    eat_A, eat_B = 0, 0

    if C < 3: return -1

    if B >= C:
        eat_B = B - (C - 1)
        B = C - 1
        if B < 1: return -1

    if A >= B:
        eat_A = A - (B - 1)
        A = B - 1
        if A < 1: return -1

    return eat_A + eat_B

for tc in range(1, T + 1): print(f'#{tc} {increasing_candy_sequence()}')

'''
전략
3가지 경우 -> 함수로 만들어서 return 처리
1. 이미 만족하는 경우 return 0
2. 사탕을 먹고 조건에 만족하면 return eat_A + eat_B
3. 조건에 만족하지 않으면 return -1

강사님 코드
def get_eating(A, B, C):
    # 1. 이미 만족 하는 경우
    if A < B < C:
        return 0

    # 사탕 개수 계산
    # 예를들어 B=5, C=5 5 - (5 - 1) | B - (C - 1), 1개먹어야한다
    # B=6, C=5인 경우 6 - (5 - 1) | B - (C - 1), 2개먹어야한다

    eat_B = max(0, B - C + 1)
    new_B = B - eat_B

    eat_A = max(0, A - new_B + 1)
    new_A = A - eat_A

    # 2. 조건을 만족하는지 확인 if - else
    if 0 < new_A < new_B < C:
        return eat_A + eat_B
    else: # 3. 조건을 만족하지 않는 경우
        return -1

T = int(input())
for tc in range(1, T + 1):
    A, B, C = map(int, input().split())
    result = get_eating(A, B, C)
    print(f'#{tc} {result}')
'''