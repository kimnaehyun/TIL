arr = ['A', 'B', 'C', 'D', 'E']
path = []
n = 3

def KFC(lev, start):
    if lev == 3:return print(*path)
        
    for i in range(start,len(arr)):
        path.append(arr[i])
        KFC(lev + 1, i + 1)
        path.pop()
        

KFC(0,0)