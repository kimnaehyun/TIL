# 테스트 케이스 메모장에서 읽어오기

import sys
sys.stdin = open('input.txt')

# stack

## 1222. [S/W 문제해결 기본] 6일차 - 계산기1

```python
def infix_to_postfix(tokens):
    stack = []          # 최종 출력이 쌓일 스택
    oper_stack = []     # 연산자들이 거쳐갈 스택

    for token in tokens:
        # 만약 token 이 숫자라면
        if token.isdigit():
            stack.append(token)
        # 숫자가 아니라면
        else:
            # oper_stack 에 연산자가 들어있다면
            # - 기존 연산자를 stack 으로 이동
            # - 현재 연산자를 oper_stack 에 저장
            # 비어있다면
            # - 현재 연산자를 oper_stack 에 저장
            if oper_stack:
                stack.append(oper_stack.pop())

            oper_stack.append(token)

    stack.append(oper_stack.pop())  # 남은 연산자 하나

    return stack


def get_result(tokens):
    stack = []
    # 전체 token을 보면서
    # - 숫자라면 stack 에 쌓는다
    # - 연산자라면, stack 에서 숫자 2개 꺼내서 계산한다.
    #   - 계산 결과를 다시 stack에 쌓는다.
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))  # 계산하기 위해서 int 로 변환
        else:
            num1 = stack.pop()
            num2 = stack.pop()

            stack.append(num1 + num2)

    return stack[0]


for tc in range(1, 11):
    N = int(input())
    row = input()
    postfix = infix_to_postfix(row)
    result = get_result(postfix)
    print(f'#{tc} {result}')
```

## 1223. [S/W 문제해결 기본] 6일차 - 계산기2

```python
# 차이점1. 우선순위를 비교할 수 있어야 한다
priority = {'+': 1, '*': 2}


def infix_to_postfix(tokens):
    stack = []          # 최종 출력이 쌓일 스택
    oper_stack = []     # 연산자들이 거쳐갈 스택

    for token in tokens:
        # 만약 token 이 숫자라면
        if token.isdigit():
            stack.append(token)
        # 숫자가 아니라면
        else:
            # oper_stack 안에 있는 연산자들 중에서
            # token 보다 우선순위가 높거나 같은 연산자들을
            # 위에서부터 순서대로 stack 으로 이동
            while oper_stack and priority[oper_stack[-1]] >= priority[token]:
                stack.append(oper_stack.pop())

            oper_stack.append(token)

    # 남은 연산자들을 모두 stack 으로 이동
    while oper_stack:
        stack.append(oper_stack.pop())

    return stack


def get_result(tokens):
    stack = []
    # 전체 token을 보면서
    # - 숫자라면 stack 에 쌓는다
    # - 연산자라면, stack 에서 숫자 2개 꺼내서 계산한다.
    #   - 계산 결과를 다시 stack에 쌓는다.
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))  # 계산하기 위해서 int 로 변환
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            if token == '+':
                stack.append(num1 + num2)
            elif token == '*':
                stack.append(num1 * num2)

    return stack[0]


for tc in range(1, 11):
    N = int(input())
    row = input()
    postfix = infix_to_postfix(row)
    result = get_result(postfix)
    print(f'#{tc} {result}')
```

## 1224. [S/W 문제해결 기본] 6일차 - 계산기3

```python
# 우선순위표
priority = {'(': 0, '+': 1, '*': 2}


# 1. 중위 -> 후위표기법으로 바꾸는 함수
def infix_to_postfix(tokens):
    stack = []  # 후위표기법 최종 결과
    oper_stack = []  # 연산자들이 중간에 거쳐갈 스택

    for token in tokens:
        # 1. 숫자라면, 그냥 stack 에 쌓는다
        if token.isdigit():
            stack.append(token)
        # 3. 여는 괄호면 oper_stack 에 추가
        elif token == '(':
            oper_stack.append(token)
        # 4. 닫는 괄호면, 여는 괄호를 만날 때 까지 연산자를 하나씩 스택으로 이동
        elif token == ')':
            while oper_stack and oper_stack[-1] != '(':
                stack.append(oper_stack.pop())
            oper_stack.pop()

        # 2. 연산자라면
        else:
            # oper_stack 에 남아있는 연산자들 중에서
            # 나보다 우선순위가 높거나 같은 연산자들을
            # stack 으로 이동 (반복문)
            # [주의] 반복하면서 pop()을 하는 경우, 항상 데이터가 있는 지 함께 체크
            while oper_stack and priority[oper_stack[-1]] >= priority[token]:
                stack.append(oper_stack.pop())

            oper_stack.append(token)

    # 남아 있는 연산자들을 뒤에서부터 스택으로 이동
    while oper_stack:
        stack.append(oper_stack.pop())

    return stack


# 2. 후위표기법을 계산하는 함수
def calculate(tokens):
    stack = []

    for token in tokens:
        # 숫자라면, stack 에 넣는다
        if token.isdigit():
            stack.append(int(token))
        # 아니라면, stack 에서 숫자 2개를 꺼내서 계산한다.
        # - 계산 결과를 stack 에 넣어준다.
        else:
            num1 = stack.pop()
            num2 = stack.pop()

            # +, * 두 가지 연산이 존재
            if token == '+':
                stack.append(num1 + num2)
            else:
                stack.append(num1 * num2)

    # stack 에 남은 최종 결과를 return
    return stack[0]


for tc in range(1, 11):
    N = int(input())
    row = input()
    postfix = infix_to_postfix(row)
    result = calculate(postfix)
    print(f'#{tc} {result}')
```

# 내일은 queue
