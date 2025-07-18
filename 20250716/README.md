# 앵커 링크

- [헤더적기](#헤더적기)
- [코드블럭](#코드블럭)
- [네이버](https://www.naver.com)


# 헤더1
## 헤더2
### 헤더3
#### 헤더4
헤더가 아닌 글씨

---


# ordered 리스트
1. 엔터를 눌러보세요
2. 탭을눌러보세요
   1. 탭을 누르면 2-1번
3. 3번

# unordered 리스트
* -기호 또는 +기호 또는 *기호 상관없습니다
* 엔터
* 대시

# 체크 리스트 만들기

- [x] 당근
- [ ] 양파
- [ ] 마늘


# 코드 블럭(백틱 3번) --> 왜 많이 쓸까?
프로그래밍 언어마다 다른 가독성으로 표시해 준다.

```python
def func(a, b):
    return a + b


a, b = int(input())
c = func(a, b)
print(c)
```

# 링크 url 걸기
[네이버](https://www.naver.com)

# 이미기 걸기
![스크린샷](./screenshot1.jpg)
![강아지](https://www.tipperarycoco.ie/sites/default/files/styles/localgov_535x302/public/2024-04/Happy%20dog.jpg?itok=uhdQ2Z1G)


# 글꼴 굵게 표시

__굵은 글씨__

중간에 **굵은 글씨**를 넣기

# 기울기

_기울기 글씨_

중간에 *기울기 글씨*를 넣기

# 굵게 및 기울임

___굵게 및 기울임___

중간에 ***굵게 및 기울임***을 넣기


# 취소선
~~박보검~~

# 수평선
---


GUI : 그래픽 유저 인터페이스
TUI : 텍스트 (이말은 잘 안씁니다.)

CLI : Command Line Interface

interface : 대상을 제어하는 수단 ( ex) 리모컨) )

---

Window OS의 Interface
GUI : Windows Shell
CLI : cmd(명령프롬프트), Power Shell

Linux OS의 Interface
GUI : GNOME
CLI : bash

왜 굳이 bash를 쓸까??
bash가 편해서 ---> Tab키 자동완성

Git을 다룰때 Interface
GUI : Github Desktop, 소스트리
CLI : git bash

결론 : GUI, CLI 둘다 쓸수는 있어야하지만 우리는 CLI를 쓸겁니다.

GUI의 장점 : 그래프 같은 복잡한 분석 보기 편하다
CLI의 장점 : 빠르다(Commit 명령어 3~4초면 끝)

---

리눅스는 항상 HOME 디렉토리에서 시작 : ~
. : 현재 디렉토리
cd ~ : 홈 디렉토리
cd .. : 상위 디렉토리
cd - : 뒤로가기

touch : 파일생성
mkdir : 폴더생성
start : 파일 열기
rm : 파일 삭제
rm -rf : 폴더 삭제
cp : 복사

절대경로
~/Desktop/test/python/

상대경로(현재 티렉토리를 기준)
cd ./python
cd ../python2

---

python.org ---> python 설치 ---> 3.11.9
인터프리터

extension??
너 IDE 뭐써??
vscode는 IDE일까??
vscode는 텍스트 에디터 : 여기에 extension을 추가해서 마치 IDE처럼 쓴다.

IDE
Python : Pycharm, jupyter notebook
C : Visual Studio
Java : IntelliJ

node.js ---> 런타임
js 백엔드 프레임워크 ---> express.js 

---

Markdown : 로직 X 
README.md에 활용
: 내가 공부한내용, 프로젝트에 대한 간단한 설명(가독성, 편의성)

---

git init  : git 시작 (로컬 저장소 생성)
rm -rf .git : git 삭제(git 종료)

git add . : staging area에 변경사항 올리기
git status : staging area의 작업 파일 확인

git config --global user.email "이메일주소"
git config --global user.name "이름"
git config --global -l

git commit -m "메시지명" : repository에(staging area의 변경사항을)올리기
git log : repository 작업 파일 확인 (커밋 이력 확인)

---

참고자료 

git commit --amend : vim 에디터가 열린다

수정 후(커서 위치를 확인 후 과감하게 타이핑)

ecs -> :q -> 저장하지 않고 종료
ecs -> :q! -> 저장하지 않고 강제 종료
ecs -> :wq -> 저장하고 종료

