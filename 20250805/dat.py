arr = [2, 1, 4, 4, 2, 2, 1]

dat = [0] * 5
idx = 0

for i in range(len(arr)):
    idx = arr[i] # 값을
    dat[idx] += 1 # 인덱스로 쓴다 (카운팅)

for i in range(len(dat)): #0, 1, 2, 3, 4만 반복
    if dat[i] > 0: print(f'{i} : {dat[i]}')
