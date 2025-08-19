# 저번주 내용 복습

20250814 폴더의 README.md 참고 (사진 있음)

# 중복순열

```python
path = []

def KFC(level):

    if level == 2: # level : 2
        print(path) # 정점 레벨에 도달했을 때
        return

    for i in range(3): # 0, 1, 2 branch : 3
        path.append(i)
        KFC(level + 1)
        path.pop()
```

# 순열(중복순열에 used배열 추가)

## 주사위 3개를 던져 나올수 있는 순열

```python
path = []
used = [0] * 7

def KFC2(level):
    if level == 3: # level : 3
        print(path)
        return

    for i in range(1, 7): # branch : 6
        if used[i] == 1: continue
        used[i] = 1 # used 배열에 기록
        path.append(i)
        KFC2(level + 1)
        path.pop()
        used[i] = 0 # used배열 기록 지워주기
```

# 부분집합은 항상 branch : 2인 중복순열 ('O', 'X')

## 5명으로 이루어진 부분집합 : level : 5

```python
arr = ['O', 'X']
path = []
name = ['A', 'B', 'C', 'D', 'E']

def print_name():
    for i in range(5):
        if path[i] == 'O':
            print(name[i], end = ' ')
    print()


def KFC3(level):

    if level == 5:
        print_name()
        return

    for i in range(2): # branch : 2
        path.append(arr[i])
        KFC3(level + 1)
        path.pop()
```

# 조합

## a b c와 b a c는 같은 조합

## 핵심 : 앞에서 뽑았던 경우의수를 제외하고 시작(start 매개변수 추가)

## 5명중에 3명 뽑는다

## level : 3, branch : 최대 5

```python
arr = ['A', 'B', 'C', 'D', 'E']
path = []

def KFC4(level, start):
    if level == 3:
        print(path)
        return

    for i in range(start , 5): # branch : 최대 5
        path.append(arr[i])
        KFC4(level + 1, i + 1)
        path.pop()
```
