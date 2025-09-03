t = int(input())

def binary_number():
    n, m = map(int, input().split())
    if m == 0: return 'OFF'
    d = 0
    for i in range(n):
        d += 2**i

    if(m - d) % 2: return 'OFF'
    else: return 'ON'

for tc in range(1, t + 1):print(f'#{tc}',binary_number())

'''
def binary_number():
    n, m = map(int, input().split())
    d = (1 << n) - 1  # 2^n - 1
    if m & d == d:
        return "ON"
    else:
        return "OFF"

for tc in range(1, t + 1):
    print(f'#{tc} {binary_number()}')
'''
 
'''
강사님 코드
# 첫 번째 방법
T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())

    TOGGLE = "ON"
    for i in range(N):
        if M & (1 << i):
            continue
            
        TOGGLE = "off"
        break

    print(f'#{tc} {TOGGLE}')

# 두 번째 방법
def solve():
    tar = M
    for i in range(N):
        if tar & 0x1 == 0:
            return 'OFF'

        tar >>= 1 # N번 반복하면서 오른쪽으로 한번씩 민다. M의 1비트가 1인지 확인
    return 'ON'

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    print(f'#{tc} {solve()}')
'''