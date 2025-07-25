# ctrl 누른 상태에서 마우스 좌클릭
# print 내장 함수의 end옵션 default는 줄바꿈
# print 내장 함수의 sep옵션 default는 공백
print('hello', end = ' ')
print('world')

# 변수에 값이 저장된다는 개념이 아니다.
# 변수에 값이 할당된다. 값은 메모리 주소를 가르키고, 메모리를 참조한다.
degree = 36.5
print(id(degree))

# 재할당하면 메모리 주소가 바뀐다. 
degree = 36.6
print(id(degree))





# 변수명 규칙 : 숫자로 시작할 수 없다.
# 언더스코어 가능 _
# 키워드 사용 불가능 (if, for)
# 내장함수나 메서드 가급적 사용 하지 않는다
# 대소문자는 서로 다른 유니코드값을 가지고 있다.

lst = [1, 2, 3]
sum = 7 # 에러는 나지 않지만 가급적 사용하지 않는다
print(sum(lst))


a = 2
b = 2.0
c = 3 + 2j
d = '1'

# 정수(int) : 음의정수, 양의정수, 0
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 1억을 지수표현법으로
num = 1e8
print(num)

# 우선순위는 음의 부호보다 거듭제곱의 우선순위가 더 높다!!
num = -2 ** 2
print(num)

# 공백도 유니코드 값을 가진다.
space = ' '
print(ord(space))


name = '장상호'
age = 20
height = 185.76

print(f'이름은 {name}이고, 나이는 {age}살, 키는 {height:.1f}')


# 시퀀스타입
# 리스트 : 가변시퀀스
arr = [1, 2, 3, 4]
arr[0] = 10
print(arr)
# 문자열 : 불변시퀀스
char = "hello"
char[0] = 'y'
print(char)


char = 'Hello World'

length = len(char)
print(length)
print(char[0], char[-1])
print(char[::2])
print(char[::-1])

# vscode 단축키 정리
ctrl + ` : 터미널 열고 닫기 \n
ctrl + b : 사이드바 열고 닫기
ctrl + s : 저장
ctrl + w : 창 닫기
ctrl + a : 전체 블록 지정
ctrl + l : 한줄 블록 지정
ctrl + / : 주석
home키, end키
shift + tab : 들여쓰기 취소
ctrl + , : settings
ctrl + shift + f : 전체 파일에서 찾기
ctrl + shift + p : 명령 팔레트
ctrl + shift + l : 특정단어 전체 수정
ctrl + h : 바꾸기
alt + shift + 방향키 : 한줄 복사 붙여넣기
alt + 마우스 좌클릭 : 커서 여러개
ctrl + alt + 방향키 : 커서 여러개
