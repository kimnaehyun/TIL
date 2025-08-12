T = int(input())

def remove_repeat_message():
    arr = list(input())
    stack = []
    for i in range(len(arr)):
        if not stack: stack.append(arr[i])
        else: 
            if stack[-1] == arr[i]: stack.pop()
            else: stack.append(arr[i])
    return len(stack)


for tc in range(1, T + 1): print(f'#{tc}', remove_repeat_message())
# 반복 문자 지우기 구현 방법
# 1. 처음에 'A' 들어올 때
#    stack = [] (비어있음)
#    -> stack.append('A')
#    stack = ['A']

# 2. 'B' 들어 올 때
#    stack = ['A']
#    -> stack.append('B')
#    stack = ['A', 'B']

# 3. 첫 번째 'C'가 들어올 때
#    stack = ['A', 'B']
#    -> stack.append('C')
#    stack = ['A', 'B', 'C']

# 4. 두 번째 'C'가 들어올 때 
#    # 스택이 비어있지 않고, 스택의 마지막 문자와 현재문자가 같은지 확인    
#    stack = ['A', 'B', 'C']
#    stack[-1] == 'C' (마지막 문자와 현재 문자 같음)
#    -> stack.pop()
#    stack = ['A', 'B']

# 5. 마지막 'B'가 들어올 때
#    stack = ['A', 'B']
#    stack[-1] == 'B' (마지막 문자와 현재 문자가 같음)
#    -> stack.pop()
#    stack = ['A']