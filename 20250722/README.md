
# 리스트 : 가변 시퀀스 -> 알고리즘에 많이 쓰임 
# 인덱싱, 슬라이싱
arr = [1, 2, 3, [4, 5, 6]]
print(arr[3][0])
print(arr[3][:])
print(arr[3][::-1])

# len 함수(내장함수일까? 메서드일까?)
print(len(arr))


# 리스트의 할당 개념 (추후에 깊은 복사 얕은 복사의 개념에 중요함)
arr = [1, 2, 3, 4]
print(id(arr)) 
arr[3] = 7 # 재할당 X
print(id(arr)) # 메모리 주소가 같다
arr = [5, 7, 4] # 재할당 O
print(id(arr)) # 메모리 주소가 다르다



# 튜플 : 불변 시퀀스(리스트와의 차이는 불변이다!!)
# my_tuple = (1, 2, 3, 4, 5)

# 특징 1
# 안정성 ---> 보안성
# 리스트만 쓰면 될것같은데 굳이 튜플을 쓸까??
# 빠르다 == 시간복잡도상 효율적이다.

# 방향배열 자료구조
# y방향, x방향
# direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 특징 2

x, y = 1, 2 # 튜플이 생략되어 있다.
x, y = (1, 2)

def kfc(x, y, z):
    return x, y, z # 튜플이 생략되어 있다.
    # return (x, y, z)

x, y, z = 1, 2, 3

print(kfc(x, y, z))




# range(start, end, step) : 불변 시퀀스
# 1. step이 양수
# start부터 end - 1까지 step만큼 증가
# 2. step이 음수
# start부터 end + 1까지 step만큼 감소 
# 핵심은 항상 수직선 상에서 end를 포함하지 않는다!!!

# 예) n번 반복하는 반복문을 만들고 싶다
# for i in range(n):



# 딕셔너리 : 가변비시퀀스
# 리스트에는 인덱스 -> 딕셔너리에는 key가 인덱스를 대신
# 핵심 : 딕셔너리는 비시퀀스이기때문에 key로 접근을 한다!!
# 딕셔너리 초기화 2가지 방법

# 1. 하드코딩
my_dict = {"apple": 2, "banana": 5, "peach": 4}

# 2. key로 접근
d = dict() # 빈딕셔너리
d["apple"] = 2
d["banana"] = 5
d["peach"] = 4

# Q) d = {} 딕셔너리? 세트?  ---> 빈 딕셔너리
# s = set() ---> 빈 세트


print(my_dict["banana"])

print(my_dict.keys()) # key만 출력
print(my_dict.values())
print(my_dict.items()) # key와 value 출력

# 1번이 3개, 2번이 2개, 5번이 6개
dat = [0, 3, 2, 0, 0, 6]

# 만약 인덱스를 못쓰고 apple이 3개
# ---> 딕셔너리
my_dict = {"apple": 3}


# 세트 가변비시퀀스
# 세트의 특징 : 중복을 허용하지 않는다 ex) 로또

# my_set = {1, 2, 3, 4}
# my_set.add(5)
# print(my_set)


# None 타입 (빈 문자열과는 다르다)
a = None
b = ""

print(type(a))
print(type(b))


# bool 타입
print(bool(3)) # 0을 제외한 모든 정수는 True
print(bool(0.0))
print(bool("")) # 빈문자열을 제외한 모든 문자열 True


# 명시적 형변환
num = '3.5'
num = int(float(num)) # int는 버림

print(num)


# 복합 연산자
# a가 1씩증가
a = 3
# a = a + 1 # 이렇게 하지 말기 무조건 복합연산자 쓰기
a += 1


# 비교연산자
# 주의 1. 항상 부등호 먼저
# => X ---> >= O
# print(3 => 2)

# 주의 2. !는 부정의 의미를 갖고 있다.
# print(3 != 2) # 3과 2는 같지 않다
# print(not(True))


# 단축평가 : and는 둘다 참이어야 참, or은 둘중 하나라도 참이면 참
# print(0 or 3 or 8) ???
# print(2 and 3 and 8) ???
# print(7 or 0 or 8) ???


# 후행 쉼표
x, y = 1, 2 # 튜플이 생략 O

x = 1 # 튜플 X
x = (1, ) # 튜플
