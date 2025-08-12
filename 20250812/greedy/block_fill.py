n = int(input())

blocks = list(map(int, input().split()))

blocks.sort()

count, total = 0, 0

for block in blocks:
    total += block
    # 카운팅하기 전에 브레이크
    if total > 100: break
    count += 1
    
print(count)