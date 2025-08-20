# - 화덕의 맨 앞의 피자를 꺼내서 치즈확인(popleft())
# - 치즈의 양 반으로 줄이기 (// : 몫)
# - if 치즈가 0이면 새 피자를 화덕에 넣기(oven.append(pizzas.popleft()))
#- else : 치즈가 남아있으면 -> 다시 화덕에 넣기 (oven.append())
# - 화덕에 피자가 한개 남을때까지 반복 (while문)
# - 마지막에 남은 피자 번호 출력 oven[0][0]
# - deque == [피자 인덱스, 치즈의 양]

import os 
import sys
from collections import deque

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(current_dir, 'sample_input(1).txt')

sys.stdin = open(input_file)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # N : 화덕 크기, M : 피자 개수
    cheese = list(map(int, input().split()))
    # 인덱스 1부터 시작(+1), 치즈양
    pizzas = deque([[i + 1, p] for i, p in enumerate(cheese)])

    oven = deque() # 화덕
    for _ in range(N): # 처음에 화덕에 피자를 N개 넣음
        if pizzas: oven.append(pizzas.popleft())

    # 화덕에 피자가 한 개 남을때 까지 반복
    while len(oven) > 1:
        now = oven.popleft() # 화덕에서 피자하나 꺼냄
        # now = [피자인덱스, 치즈의양]
        now[1] //= 2 # 꺼낸 피자의 치즈 양을 절반으로 줄이고
        if now[1] == 0: # 치즈가 모두 녹았다면
            if pizzas: # 남은 피자가 있으면
                oven.append(pizzas.popleft()) # 새 피자 넣기
        else: # 치즈가 아직 남아있다면 다시 화덕에 넣기
            oven.append(now)

    # while문 종료후 피자 한개만 남아있음. 피자의 번호 출력
    # [피자인덱스, 치즈의 양]
    print(f'#{tc} {oven[0][0]}')