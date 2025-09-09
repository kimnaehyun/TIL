T = int(input())

def telephone_pole():
    N = int(input())
    arr = []
    count = 0
    for i in range(N):
        start, end = map(int, input().split())
        if i:
            for prev_start, prev_end in arr:
                if start < prev_start and end > prev_end: count += 1
                if start > prev_start and end < prev_end: count += 1
        arr.append((start, end))
    return count

for tc in range(1, T + 1): print(f'#{tc} {telephone_pole()}')


'''
강사님 코드
def get_result():
    size = len(arr)
    cnt = 0

    for i in range(size): # 기준이 되는 전봇대
        for tar in range(i): # 갯수를 세야하는 전봇대
            # a 첫번째 전봇대, b 두번째 전봇대
            i_a, i_b = arr[i][0], arr[i][1]
            tar_a, tar_b = arr[tar][0], arr[tar][1]

            if i_b < tar_b: cnt += 1

    return cnt


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr=[]
    for n in range(N):
        a, b = map(int, input().split()) # 전봇대
        arr.append((a, b))

    arr.sort(key=lambda x : x[0]) # 첫 번째 원소(a전봇대)를 기준으로 정렬
    result = get_result()
    print(f'#{tc} {result}')

'''