arr = list(map(int,input().split()))

arr.sort()

value = 0

for i in range(len(arr)):
    if len(arr) - i - 1 != 0: value += arr[i] * (len(arr) - i -1)
    
print(value)