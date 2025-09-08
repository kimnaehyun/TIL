import sys
import os

file_path = os.path.join(os.path.dirname(__file__), "sample_input.txt")
sys.stdin = open(file_path, "r", encoding="utf-8")

arr = list(map(int, input().split()))
path = []
n = 6 
used = [0] * n
arr1 = []

def permutation(lev):
    if lev == n:
        arr1.append(path[:])
        return
    
    for i in range(n):
        if used[i]: continue
        path.append(arr[i])
        used[i] = 1
        permutation(lev + 1)
        path.pop()
        used[i] = 0


permutation(0)

cnt = 0

def is_run(arr):
    arr = sorted(arr)
    return arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]

def is_baby_gin(p):
    global cnt
    start = [p[0], p[1], p[2]]
    end = [p[3], p[4], p[5]]

    if start[0] == start[1] == start[2]: cnt += 1
    elif is_run(start): cnt += 1

    if end[0] == end[1] == end[2]: cnt += 1
    elif is_run(end): cnt += 1

    if cnt == 2: return True
    cnt = 0
    return 


for i in arr1:
    if is_baby_gin(i): 
        print('Yes')
        break
else: print('No')

'''
used = [0] * 6
path = []
is_babygin = 0

def is_baby_gin():
    cnt = 0
    # 앞에 세자리가 triplet 또는 run
    a, b, c = path[0], path[1], path[2]
    if a == b == c: cnt += 1
    elif (a) == (b - 1) == (c - 2) : cnt += 1

    # 뒤에 세자리가 triplet 또는 run
    a, b, c = path[3], path[4], path[5]
    if a == b == c: cnt += 1
    elif (a) == (b - 1) == (c - 2) : cnt += 1

    return cnt == 2 # cnt 가 2면 baby-gin이 맞다!

# 순열 코드
def recur(lev):
    global is_babygin
    if lev == 6: # level은 6
        if is_baby_gin():
            is_babygin = 1
        return

    for i in range(6): # branch는 6
        if used[i] == 1: continue
        used[i] = 1
        path.append(arr[i])
        recur(lev + 1)
        path.pop()
        used[i] = 0

arr = list(map(int, input().split()))
recur(0)

if is_babygin: print('Yes')
else: print('No')

'''