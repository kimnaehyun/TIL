arr = [[] for _ in range(5)]

arr[0] = [1, 3, 4]
arr[1] = [2, 3]
arr[3] = [2, 4]
arr[4] = [1, 3]

n = int(input())
s = 'DUSRK'
for i in arr[n]: print(s[i])