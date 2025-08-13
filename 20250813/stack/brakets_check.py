T = int(input())

def is_brakets():
    text = input()
    stack = []
    
    for char in text:
        # 1. 여는 괄호면 스택에 추가
        if char == '(' or char == '{': stack.append(char)
        # 2. 닫는 골호가 소괄호면 스택에 비어있지 않고, 짝이 맞는지 확인 후 제거
        elif stack and char == ')' and stack[-1] == '(': stack.pop()
        # 3. 닫는 골호가 중괄호면 스택에 비어있지 않고, 짝이 맞는지 확인 후 제거
        elif stack and char == '}' and stack[-1] == '{': stack.pop()
        # 4. 닫는 괄호인데 짝이 맞지 않는다. -> 스택에 추가
        elif char == ')' or char == '}': stack.append(char)
    # 스택이 비어있지 않으면 0, 비었으면 1
    return 0 if stack else 1


for tc in range(1, T + 1): print(f'#{tc}', is_brakets())