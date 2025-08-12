N = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
sum_v = 0

# 1개 이하가 될때까지 반복
while len(arr) > 1:
    # 작은거 두개 빼서 더하고
    temp = arr.pop() + arr.pop()
    # 합계누적
    sum_v += temp
    # append로 넣고
    arr.append(temp)
    # 다시 정렬
    arr.sort(reverse=True)
    
print(sum_v)