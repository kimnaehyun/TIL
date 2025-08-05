def counting_sort(data, temp, k):
    # data [] -- 입력 배열(원소는 0 이상 k 이하 정수)
    # temp [] -- 정리된 배열
    # counts [] -- 카운트 배열

    counts = [0] * (k + 1)
    
    # 1단계 counting
    for i in range(len(data)):  # data[i] 발생횟수 기록
        counts[data[i]] += 1

    # 2단계 counts 값 조정(누적)
    for i in range(1, k + 1):
        counts[i] += counts[i-1]

    # 3단계 뒤에서부터 정렬된 배열 생성
    for i in range(len(data), -1, -1):
        counts[data[i]] -= 1
        temp[counts[data[i]]] = data[i]

    return temp


arr = [12, 3, 9, 1, 15, 7]

counting_sort(arr, [0] * len(arr), max(arr))
