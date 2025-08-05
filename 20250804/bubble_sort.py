arr = [12, 3, 9, 1, 15, 7]

def bubbleSort(a, l):
    for i in range(l - 1, 0, -1):        
        for j in range(0, i):         
            if a[j] > a[j + 1]:        
                a[j], a[j + 1] = a[j + 1], a[j]  

bubbleSort(arr, len(arr))

print(*arr)
