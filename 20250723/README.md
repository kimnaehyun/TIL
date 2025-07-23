# 출력하는방법, 입력받는방법
# input()
# Q) input()을 실무에서 쓸까??
# A) 실무에서는 input을 쓰지 않습니다.
# Q) 그런데 input()을 왜 배워야 할까?
# A) 프로그래밍 언어를 익히는데 가장 빠른방법 : 알고리즘 문제 풀기

# 1. 문자열 입력받기
```char = input()```

# 2. 정수 입력받기
```num = int(input())```

# 3. 정수 2개 입력받아서 각각의 변수에 할당
# map함수, split()메서드
# map함수를 쓰는 목적 : 정수로 변환 
```a, b = map(int, input().split())
print(a, b)```

# 4. 정수 여러개를 입력받아서 리스트에 할당
```arr = list(map(int, input().split()))
print(*arr)```

# 5. 심화 2차원 리스트를 입력받기 (D3 난이도)
# 3x3 행렬
# 반드시 어떤 로직을 써야할까? : 중첩 반복문
# ---> 리스트 컴프리헨션


```result = []
for _ in range(3): # 3행
    arr = list(map(int, input().split()))
    result.append(arr) # 행 추가, 행 추가, 행 추가

print(result)```


arr = [list(map(int, input().split())) for _ in range(3)]
print(arr)


# 재귀 함수란?
# 이 함수가 재귀함수다! 어떻게 알수 있을까?
# 1. 재귀 호출(자기 자신을 호출)이 있으면 재귀 함수
# 단 주의 : 무한 loop에 빠질 수 있다.
# 무한 loop를 막으려면?
# 2. 기저 조건(종료 조건) - return

def kfc(lev):
    # 2. 기저 조건
    if lev == 2:
        return
    print(lev)
    # 1. 재귀 호출 2번
    kfc(lev + 1)
    kfc(lev + 1)
    print(lev)

kfc(0)



# sort()와 sorted()의 차이??
# 공통점 : 정렬(오름차순)
arr = [1, 2, 3, 4, 5]

# 반환 X, 원본 변경 ---> sort()
arr.sort()
# 반환 O, 원본 변경 X ---> sorted()
sorted_arr = sorted(arr, reverse=True) # 내림 차순



# 전역변수 vs 지역변수
# Q) global 사용 이유?
# A) 지역 변수로 사용하면 호출할때마다 지역변수가 초기화 되기 때문에

a = 30 # global scope # 10으로 수정

def kfc():
    global a # global 쓰는 목적? # 전역변수를 수정 하고 싶을 때
    a = 10 # local scope
    b = 20 # local scope
    print(a) # 10

kfc()
print(a) # 10 # built-in scope


# map 함수란?
# a, b = map(int, input().split())
# map(첫번째 인자==함수, 두번째 인자==iterable)

# iterable이란??

arr = [1, 2, 3, 4]

char = "hello"

my_tuple = (1, 2, 3)

my_dict = {"apple": 1, "banana": 2, "grape": 3}

my_set = {1, 2, 3}

# 시퀀스(순서가 있는, 인덱스가 있는) == iterator (X)
# iterable : 반복 가능한 객체

for i in arr: # iterator 방식으로 순회했다.
    print(i, end = ' ')

for i in char:
    print(i, end = ' ')

for i in my_tuple:
    print(i, end = ' ')

for i in my_dict: # key를 기준으로 순회
    print(i, end = ' ')

for i in my_set: # hash값이 작은 순서대로 순회
    print(i, end = ' ')

# itertor : 반복 가능한 객체