'''
t = int(input())

for tc in range(1, t + 1):
    n = float(input())
    result = ""

    for _ in range(12):  # 최대 12자리
        n *= 2
        if n >= 1:
            result += "1"
            n -= 1
        else:
            result += "0"

        if n == 0:  # 정확히 떨어짐
            break

    if n != 0:  # 12자리 넘어가도 끝나지 않음
        print(f"#{tc} overflow")
    else:
        print(f"#{tc} {result}")

'''
'''
# 강사님 코드
def change(n):
    binary = ""
    power = -1 # 2의 -1제곱부터 시작
    cnt = 0

    while n > 0 and cnt < 13:
        value = 2 ** power  # 2의 -1제곱, 2의 -2제곱....

        if n >= value: # 현재 자리값을 뺄 수있다.
            binary += "1" # 이진수 1
            n -= value # 값 빼주고
        else:
            binary += "0" # 자리값을 뺄수 없으면 0

        power -= 1
        cnt += 1

    if n > 0: # 계산이 끝났는데도 n이 남아있으면
        return 'overflow'
    else:
        return binary

T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    result = change(N) # 함수호출
    print(f'#{tc} {result}')
'''