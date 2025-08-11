T = int(input())

def sequence1():
    N = int(input())
    str = input()
    big_count = 0
    count = 0
    for s in str:
        if s == '1':
            count +=1
            if big_count < count:
                big_count = count
        else:count = 0
    return big_count

for t in range(T):print(f'#{t + 1} {sequence1()}')
        