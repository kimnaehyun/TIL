arr = [[] for _ in range(3)]
arr[0] = ['A', 'B', 'T']
arr[2] = ['R', 'S']

for i in arr: print(''.join(reversed(i)))