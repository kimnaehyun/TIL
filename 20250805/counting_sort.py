def counting_sort(result):
    dat = [0] * (k + 1)
    # 1단계 counting
    for i in range(len(arr)):
        dat[arr[i]] += 1
    # 2단계 dat값 조정(누적)
    for i in range(1, k + 1):
        dat[i] += dat[i-1]
    # 3단계 뒤에서부터 정렬된 배열 생성
    for i in range(len(arr)-1, -1, -1):
        dat[arr[i]] -= 1
        result[dat[arr[i]]] = arr[i] # 0으로 채워져 있어야 인덱싱 가능

arr = [12, 3, 9, 1, 15, 7]
k = 15
result = [0] * len(arr) # global 쓰던지 아니면 매개변수로 들어가던지
# 함수호출
counting_sort(result)

print(*result)