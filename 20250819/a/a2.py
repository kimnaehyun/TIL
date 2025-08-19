# T = int(input())

arr = []

path = []

dat_arrs =[]

def KFC(lev, start, problems, correct):
    dat = [0] * problems
    
    if lev == correct: 
        for i in path:
            dat[i - 1] = 1
        dat_arrs.append(dat)
        return 
    
    for i in range(start, problems):
        path.append(arr[i])
        KFC(lev + 1, i + 1, problems, correct)
        path.pop()


def introduce():
    N, M, K = map(int, input().split())
    
    for i in range(1, N + 1): arr.append(i)

    KFC(0, 0, N, M)
    
    value = 0
    count = 0
    count_arr = []
    
    for dat_arr in dat_arrs:
        for dat in dat_arr:
            if dat: 
                count += 1
                if count % K == 0: value *= 2
                else: value += 1
            else:
                count = 0
        count_arr.append(value)
        value = 0
        count = 0
    return count_arr
 
print(min(introduce()))
