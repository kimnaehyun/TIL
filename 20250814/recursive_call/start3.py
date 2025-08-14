arr =[1, 0]
path = []
name = ['Luffy', 'Zoro', 'Sanji']

def print_name():
    arr = []
    for i in range(len(path)):
        if i == 0: 
            if path[i]: arr.append(name[i])
        elif i == 1:
            if path[i]: arr.append(name[i])
        elif i == 2:
            if path[i]: arr.append(name[i])
    return arr

def kfc(lev):
    if lev == 3: 
        print(*print_name())
        return
    for i in range(2):
        path.append(arr[i])
        kfc(lev + 1)
        path.pop()
        
kfc(0)