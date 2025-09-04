def solve():
    n, min_size, max_size = map(int, input().split())
    scores = list(map(int, input().split()))

    # 정렬
    scores.sort()
    # 최소 차이 초기화
    min_diff = float('inf')

    # 어학점수가 1점~100점
    for t1 in range(1, 101):
        for t2 in range(t1 + 1, 101):
            # 각 반의 인원수 계산
            c_cnt = 0 # t1 미만
            b_cnt = 0 # t1 이상 t2 미만
            a_cnt = 0 # t2 이상

            # 1,2,3,4번 구현
            for score in scores:
                if score < t1:
                    c_cnt += 1
                elif score < t2:
                    b_cnt += 1
                else:
                    a_cnt += 1

            # 모든 반이 최소/최대 인원의 모든 조건을 만족
            if (min_size <= a_cnt <= max_size and
                    min_size <= b_cnt <= max_size and
                    min_size <= c_cnt <= max_size):
                # 최대 인원 - 최소 인원
                max_cnt = max(a_cnt, b_cnt, c_cnt)
                min_cnt = min(a_cnt, b_cnt, c_cnt)
                diff = max_cnt - min_cnt
                # 최소 차이 갱신
                min_diff = min(min_diff, diff)

    return min_diff if min_diff != float('inf') else -1

t = int(input())
for tc in range(1, t + 1):
    result = solve()
    print(f'#{tc} {result}')
