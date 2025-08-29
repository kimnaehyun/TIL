arr = [4, 5, 1, 1, 5, 4, -3, -13, 9, 20, 13]
length = len(arr)
arr2 = [0] * length


def get_sum():
    for n in range(length): 
        if n + 4 < length: arr2[n] =  sum(arr[n:n+5])
    max_value = max(arr2)
    return arr2.index(max_value)
    

print(get_sum())


# 강사님 코드
# arr = [4, 5, 1, 1, 5, 4, -3, -13, 9, 20, 13]

# def get_sum(idx):
#     sum_v = 0
#     # 5개의 합
#     for i in range(5):
#         sum_v += arr[idx + i]# +0, +1, +2, +3, +4 인덱싱
    
#     return sum_v

# N = len(arr)
# M = 5

# max_v = float('-inf')
# for idx in range(N-M+1):
#     ret = get_sum(idx)
#     if ret > max_v: # 최대값 갱신
#         max_v = ret
#         max_idx = idx # 최대값 일때 인덱스

# print(max_idx)