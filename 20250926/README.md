관통 프로젝트
# 주식 댓글 수집 및 관리 기능 구현

## 1. 구현 과정

### (1) 댓글 크롤링 및 DB 저장

1. **Selenium을 이용한 웹 크롤링**

   * `Toss 투자` 사이트 접속 → 검색창에서 회사명 입력 → 종목 코드 추출 → 커뮤니티 페이지 이동
   * `article.comment span` 요소를 반복 스크롤하며 댓글 수집
2. **Django 모델 연동**

   * `Crawling` 모델: `company_name`, `code`, `comment` 필드
   * 수집된 댓글을 반복하며 `Crawling(company_name=..., code=..., comment=...)` 객체 생성 후 `save()` 실행
   * 이렇게 하면 댓글이 DB에 저장됨

### (2) 댓글 조회

1. `search` 뷰: GET 파라미터 `company`를 받아 DB 조회 (`Crawling.objects.filter(company_name=company)`)
2. 템플릿에서 QuerySet 반복문으로 댓글 목록 표시

   * 첫 번째 댓글 정보: `crawling.0.company_name`, `crawling.0.code`
   * 댓글 리스트 반복: `{% for c in crawling %} {{ c.comment }} {% endfor %}`

### (3) 댓글 삭제

1. `urls.py`에서 삭제 URL 지정: `path('<int:pk>/delete/', views.delete, name='delete')`
2. 삭제 뷰(`delete`) 작성:

   * pk 기준 댓글 가져오기
   * 삭제 전 `company_name` 변수 저장
   * `comment.delete()` 실행 후, `redirect(f'/crawlings/search/?company={company}')`로 같은 회사 댓글 페이지로 돌아가기

---

## 2. 학습 내용

* Selenium과 Django 모델을 연동하여 **웹 크롤링 → DB 저장**
* QuerySet의 **인덱스 접근 방법** (`crawling.0`)
* `delete()` 실행 후 **이미 변수로 할당된 값은 살아있음**
* URL 매개변수와 `reverse`/`url` 템플릿 태그 활용
* GET 파라미터를 이용한 **삭제 후 페이지 유지** 방법

---

## 3. 어려웠던 점

* 템플릿에서 리스트 인덱스 접근 시 `TemplateSyntaxError`
* 삭제 버튼 URL 매개변수 오류(`NoReverseMatch`)
* 삭제 후 페이지가 초기화되어, 사용자가 다시 검색해야 했음 → GET 파라미터 활용으로 해결

---

## 4. 새로 배운 점

* Django 템플릿의 QuerySet 접근 규칙
* 삭제 후 리다이렉트 시 변수 유지 방법
* 크롤링한 데이터를 **Django 모델로 바로 저장**
* GET 파라미터를 활용하여 **삭제 후 동일 검색 결과 유지**