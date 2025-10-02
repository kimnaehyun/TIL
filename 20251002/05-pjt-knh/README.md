# 05-PJT Django 웹 프레임워크 사용자 인증 기반 DB 설계

## 1. 프로젝트 개요

* 사용자 인증 기반 CRUD 기능을 갖춘 도서 커뮤니티 웹 애플리케이션 제작
* Django Model, Form, ORM, Authentication System 이해 및 활용

---

## 2. 프로젝트 구조

```
05-pjt/
│
├─ mypjt/              # Django 프로젝트
│  ├─ settings.py
│  ├─ urls.py
│  └─ ...
│
├─ accounts/           # 사용자 인증 앱
│  ├─ models.py
│  ├─ forms.py
│  ├─ views.py
│  ├─ urls.py
│  └─ templates/accounts/
│      ├─ login.html
│      ├─ signup.html
│      ├─ update.html
│      ├─ change_password.html
│      └─ ...
│
├─ books/              # 도서 관리 앱
│  ├─ models.py
│  ├─ forms.py
│  ├─ views.py
│  ├─ urls.py
│  └─ templates/books/
│      ├─ index.html
│      ├─ create.html
│      ├─ detail.html
│      ├─ update.html
│      └─ ...
│
└─ static/             # CSS, JS, 이미지 파일
```

---

## 3. 기능 구현 및 학습 내용

### A. accounts 앱

#### 1) User 모델 커스텀 (F02)

* `AbstractUser`를 상속받아 커스텀 모델 구현
* Django 기본 `User` 모델의 기능 유지하면서 확장 가능
* **학습 포인트:** Django에서 제공하는 인증 시스템을 직접 확장하는 방법 이해

#### 2) Form 클래스 구현 (F03)

* 로그인, 회원가입, 회원정보수정, 비밀번호 변경에 필요한 Form 생성
* 유효성 검사 및 에러 메시지 처리
* **어려웠던 점:** 기존 Form 클래스와 커스텀 Form 클래스의 상속 구조 이해

#### 3) View 함수 구현

| 기능              | URL                          | HTTP Method | 기능 설명              |
| --------------- | ---------------------------- | ----------- | ------------------ |
| login           | `/accounts/login/`           | GET/POST    | 사용자 로그인 처리, 세션 생성  |
| logout          | `/accounts/logout/`          | POST        | 세션 삭제, 로그아웃 처리     |
| signup          | `/accounts/signup/`          | GET/POST    | 회원가입 처리, 로그인 자동 수행 |
| update          | `/accounts/update/`          | GET/POST    | 로그인 사용자 정보 수정      |
| delete          | `/accounts/delete/`          | POST        | 로그인 사용자 계정 삭제      |
| change_password | `/accounts/change_password/` | GET/POST    | 비밀번호 변경, 로그인 유지    |

* **학습 포인트:**

  * GET/POST 요청에 따른 UI 제공 및 데이터 처리 분리
  * 로그인 상태에 따른 UI 변경 (네비게이션 바)
  * 세션 관리 및 사용자 인증 흐름 이해

* **어려웠던 점:**

  * `POST` 요청과 `GET` 요청을 동일 view에서 처리하면서 에러 메시지 표시
  * 로그인 상태에 따른 접근 제한 처리

---

### B. books 앱

#### 1) Book 모델 구현 (F04)

* 필드: `title`, `explanation`, `review_rating`, `author`
* `review_rating`은 0~10 범위 정수
* **학습 포인트:** Django Model 필드 타입 및 제약 조건 이해

#### 2) BookForm 구현 (F05)

* ModelForm 사용하여 입력 데이터 검증
* 유효하지 않은 입력 시 오류 메시지 표시

#### 3) View 함수 구현

| 기능     | URL                       | HTTP Method | 기능 설명                    |
| ------ | ------------------------- | ----------- | ------------------------ |
| index  | `/books/`                 | GET         | 전체 도서 조회, 상세 페이지 링크 제공   |
| create | `/books/create/`          | GET/POST    | 도서 등록, 유효성 검증 후 저장       |
| detail | `/books/<int:pk>/`        | GET         | 단일 도서 정보 출력, 수정/삭제 링크 제공 |
| update | `/books/<int:pk>/update/` | GET/POST    | 도서 수정, 이전 값 초기화, 유효성 검증  |
| delete | `/books/<int:pk>/delete/` | POST        | 도서 삭제, index 페이지로 리다이렉트  |

* **학습 포인트:**

  * Django ORM을 활용한 CRUD 구현
  * ModelForm과 view 함수의 상호작용 이해
  * URL 네이밍과 유지보수 고려

* **어려웠던 점:**

  * Form 초기값 설정과 POST 처리 시 데이터 덮어쓰기
  * 상세 페이지에서 update/delete 링크 연결

---

## 4. 비기능적 요구사항

1. **URL 구성 (NF01)**

   * `app_name`과 `path()`를 활용하여 유지보수가 용이한 URL 설계

2. **HTTP Method 제한 (NF02)**

   * GET/POST 요청에 따른 view 처리
   * 로그아웃, 삭제 등 위험 동작은 POST만 허용

---

## 5. 프로젝트 진행 후기

* **배운 점:**

  * Django의 모델, 폼, 인증 시스템을 통합적으로 이해
  * CRUD 기능과 사용자 인증 기능을 동시에 구현하며 실무 감각 향상
  * URL 설계, template 상속, 네비게이션 바 구현 등 유지보수 고려

* **어려웠던 점:**

  * 로그인 상태에 따라 다른 UI를 동적으로 보여주는 부분
  * Form validation과 초기값 설정, POST/GET 요청 처리

* **느낀 점:**

  * Django 프로젝트는 요구사항을 체계적으로 분리하면 구현이 효율적임
  * 사용자 인증과 데이터 관리 기능을 동시에 다루며 백엔드 흐름 이해