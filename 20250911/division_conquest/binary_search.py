def binary_search(arr, target):
    start = 0 # 0번 인덱스
    end = len(arr) - 1 # 끝 요소 인덱스
    flag = 0 # flag처리

    while start <= end: # start와 end가 같아질때까지
        mid = (start + end) // 2
        # 이진 탐색을 통해서 타겟을 찾으면 middle 인덱스 반환
        if arr[mid] == target:
            # return mid
            return True
        # 타겟이 중간값 보다 크면 오른쪽 부분 탐색
        elif arr[mid] < target:
            if flag == 2: break
            flag = 2
            start = mid + 1
        else: # 타겟이 중간값보다 작으면 왼쪽 부분 탐색
            if flag == 1: break
            flag = 1
            end = mid - 1
    # 타겟 못찾으면
    return False

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    b = list(map(int, input().split()))

    cnt = 0
    for num in b:
        cnt += binary_search(arr, num)

    print(f'#{tc} {cnt}')
