def get_sum(tar):
    sum_v = 0
    for i in range(N):
        if tar & 0x1: # 마지막비트가 1인지 확인
            sum_v += heights[i]
        tar >>= 1 # 타겟을 오른쪽으로 한번씩 밀면서
    return sum_v

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    min_diff = float('inf')

    for tar in range(1, 1 << N): # 2의 n제곱 개
        total = get_sum(tar)
        # 최소값 갱신
        if total >= B:
            diff = total - B
            min_diff = min(min_diff, diff)

    print(f'#{tc} {min_diff}')