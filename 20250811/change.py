N = int(input())

count = 0

count += N // 500
N %= 500

count += N // 100
N %= 100

count += N // 50
N %= 50

count += N // 10
N %= 10

print(count)