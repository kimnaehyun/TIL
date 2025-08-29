arr = [4, 5, 1, 1, 5, 4, -3, -13, 9, 20, 13]

def get_sum():
    n = int(input())
    sum_value =  arr[n:n+5]
    return sum(sum_value)

print(get_sum())