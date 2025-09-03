arr = [[] for _ in range(6)]

arr[0] = [1, 2, 3]
arr[1] = [4, 5]

s = 'ABTQVX'

n = int(input())

for i in arr[n]: print(s[i])