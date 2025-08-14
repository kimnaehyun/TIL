arr = input().split()
n = len(arr)

def get_sub(tar):
    cnt = 0
    for _ in range(n):
        if tar & 0x1: 
            cnt += 1
        tar >>= 1 
    return cnt 


result = 0

for tar in range(1 << n): 
    if get_sub(tar) >= 2: # 비트가 2개 이상 1이라면,
        result += 1

print(result)