def recur(month, sum_v):
    global result
    if month > 12: # 기저조건
        result = min(result, sum_v) # 최소비용 갱신
        return

    # 1일 이용권
    recur(month + 1, sum_v + (plans[month] * cost[0]))
    # 1달 이용권
    recur(month + 1, sum_v + cost[1])
    # 3달 이용권
    recur(month + 3, sum_v + cost[2])
    # 1년 이용권
    recur(month + 12, sum_v + cost[3])

T = int(input())
for tc in range(1, T + 1):
    cost = list(map(int, input().split())) # 이용권 가격
    plans = [0] + list(map(int, input().split()))# 월별 이용 계획 (1월부터)
    result = float('inf')
    recur(1, 0) # 1월부터 시작, 0원부터 시작
    print(f'#{tc} {result}')