n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]

# 회의가 끝나는 시간을 기준으로 정렬
# 만약 종료시간이 같다면 시작시간이 빠른 순이 우선
meetings.sort(key = lambda x: (x[1], x[0]))

count = 1
first = meetings[0][1]

for i in range(len(meetings)):
    if first <= meetings[i][0]:
        count += 1
        first = meetings[i][1]
print(count)            