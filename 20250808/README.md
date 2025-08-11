# 1. 아스키코드
## 대문자 A : 65, 소문자 a : 97
## 대문자 + 32 = 소문자

# 2. find 메서드
## (1) str.find() : 찾으면 발견된 인덱스 반환, 못찾으면 -1 반환
## (2) str.find('a', n)
## : n번 인덱스 부터 시작해서 문자 'a'를 찾아라
## ex) [123]345[87] ---> 87을 parsing하고싶다.

``` python
text = "banana"
print(text.find('a')) # 1
print(text.find('a', 2)) # 3
print(text.find('a', 4)) # 5
```

# 3. 회문 : 거꾸로 읽어도 같은 문자열
## 거꾸로 뒤집는 방법 [::-1]
``` python
text = 'level'
def is_p(text):
    return text == text[::-1] # 맞으면 1, 다르면 0 반환

print(int(is_p(text)))
```

# 19783. - boss 문제 - 괄호 친구들
![이미지](./img/img.png)