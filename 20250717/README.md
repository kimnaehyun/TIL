# 깃 기본
git : 분산 버전 관리 시스템

git : 로컬저장소 // github : 원격저장소

git init : git 시작

git add . : staging area에 올리기
git status : staging area의 작업 파일 확인

<git commit 전에>
git config --global user.name "이름"
git config --global user.email "이메일"
git config --global -l : user.name과 user.email 확인

git commit -m "메시지명" : repository에 올리기
git log : 커밋 이력을 확인

git remote add origin url : 로컬 저장소와 원격저장소를 연결(origin은 별칭)
git remote -v : remote 목록 확인

git remote rm 별칭 : remote 이력 삭제


git push origin +master : 가장 최근에 commit 되어있던 것을 강제로 push
                                 (origin:별칭, master:branch명, +:강제로 진행)

---

Q) clone과 pull의 차이점이 뭘까??
A) 새로운 환경에서 처음 다운로드 : clone

명령어 : git clone url

Q) clone을 받으면 remote를 할 필요가 있을까?
A) remote를 할 필요가 없다.

Q) clone과 pull의 차이?
A) 한번 clone을 받고 그 이후에는 pull로 진행

명령어 : git pull origin +master

---

자리 옮긴후 

1. git clonfig --global -l 확인
user.name, user.email 확인

2. 제어판 -> 사용자 계정 -> window 자격 증명 -> github, gitlab 삭제


---

Q) .gitignore 파일은 왜 만들까?
A) 수 백개의 파일을 일일이 git add 하기에는 불편하기 때문에
    .gitignore파일을 만들면 편하다

용량이 매우 크거나, 보안상 문제가 있거나, 청구 결제 관련된 파일들을
add 하지 않기 위해 .gitignore파일을 만든다(staging area에 올리지 않기 위해)

방법 : .gitignore 파일 생성 -> add 하지 않을 파일명이나 폴더명 작성하고 저장 

# 깃 심화
commit 메시지 수정하기

명령어 : git commit --amend

vim에디터에서 수정하고
esc -> :q! : 저장하지 않고 강제 종료
esc -> :wq! : 강제 저장하고 종료

---

git revert : 특정 commit을 없었던 일로 만들기

a.txt 만들고 commit
b.txt 만들고 commit
c.txt 만들고 commit

git log -> 해시값 전체 복사(ctrl + shift + c), 붙여넣기(shift + insert)

명령어 :
git revert 해시값 : 이 특정 커밋을 없었던 일로 만든다.
vim 에디터 -> esc -> :wq

---

git reset : 특정 commit으로 되돌리기

git reflog : 이전 과거 commit 기록들을 모두 볼 수 있음

명령어 : git reset --hard HEAD@{번호}

---

staging area 있는 작업을 working directory로 옮기기
(git add 취소하기)

<git 2.23 버전 이전>

1. commit이 없는 경우
git rm --cached 파일명

2. 이전에 했던 commit이 있는경우(권장 방법)
git restore --staged 파일명
