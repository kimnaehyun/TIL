 CRUD
# Create
방법은 3가지 방법

## 첫 번째 방법
article = Article()  
article.title = 'first'  
article.context = 'hello'  
article.save()  

## 두 번째 방법
article = Article(title = 'second', context = 'hello')  
article.save()  

## 세 번째 방법
Article.objects.create(title = 'third', context = 'byebye')  

### 방법 3가지가 있는데 어떤 방법을 쓸까??
3번째 방법은 절대 쓰면 안된다.(지양해야한다)  
DB에 save하기전에 반드시 유효성 검사를 해야한다.  
save()하기전에 데이터를 검증하고 그다음에 저장해야된다.  

### 가장 많이 쓰는 방법 2번
1. save()하기전에 유효성 검사도 가능하고  
2. 코드도 간결하고  

# Read
전체 데이터 조회 -> def index(request)  
Article.objects.all()  

## 특정 조건 데이터 조회(filter)
Article.objects.filter(title='first')  
Article.objects.filter(context__contains='hel')  
Article.objects.filter(title__startswith='f)  

## 단일 데이터 조회(get) -> def detail(requests), (views.py에 작성)
단일 데이터(고유성을 보장하는 조회)  
만약 조회하려는 객체가 없으면 에러발생(예외발생)  
조회하려는 객체가 2개이상 에러발생(예외발생)  
pk로 조회!!  
Article.objects.get(pk=1)  
Article.objects.get(context='hi')  

# Update -> def update(requests)
## 수정하려면 먼저 get으로 조회해야한다
article = Article.objects.get(pk=1)  
article.title = 'forth'  
article.save()  

# Delete -> def delete(requests)
삭제하기전 조회  
article = Article.objects.get(pk=1)  
article.delete()  
Article.objects.get(pk=1)  

---> 예외 발생  