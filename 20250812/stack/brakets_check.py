T = int(input())

def is_brakets():
    stack = []
    text = input()
    for char in text:
        if char == '(' or '{': stack.append(char)
        elif char == ')':
            if stack[-1] == '(': stack.pop()
            stack.append(char)
        elif char == '}':
            if stack[-1] == '{': stack.pop()
            stack.append(char)
    return len(stack) 


for tc in range(1, T + 1): print(is_brakets())