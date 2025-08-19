T = int(input())

def im():
    N = int(input())
    arr = list(map(int, input().split()))
    count = 1
    for i in range(1, len(arr) - 1):
        count += i + 1 - arr[i] + 2

    return count


for tc in range(1, T + 1): print(f'#{tc}', im())