def binary_search(arr, target):
    start, end = 0, len(arr) - 1
    last_dir = 0   # 0 = 시작, -1 = 왼쪽, 1 = 오른쪽

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            if last_dir == 1: return False # 직전에도 오른쪽
                
            last_dir = 1
            start = mid + 1
        else:
            if last_dir == -1: return False # 직전에도 왼쪽
                
            last_dir = -1
            end = mid - 1
    return False



T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0
    A.sort()
    for b in B: binary_search(A, b)
    print(f'#{tc} {cnt}')