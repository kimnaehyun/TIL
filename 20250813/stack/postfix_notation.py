T = int(input())

def forth():
    arr = input().split()
    stack = []
    for i in arr:
        if i.isdigit(): stack.append(int(i))
        elif i == '+': 
            try: stack.append(stack.pop(-2) + stack.pop(-1))
            except IndexError: return 'error'
        elif i == '*': 
            try: stack.append(stack.pop(-2) * stack.pop(-1))
            except IndexError: return 'error'
        elif i == '-': 
            try: stack.append(stack.pop(-2) - stack.pop(-1))
            except IndexError: return 'error'
        elif i == '/': 
            try: stack.append(int(stack.pop(-2) / stack.pop(-1)))
            except IndexError: return 'error'
        elif i == '.': return stack[0] if len(stack) == 1 else 'error'
    if len(stack) != 1: return 'error'
            

for tc in range(1, T + 1): print(f'#{tc}', forth())