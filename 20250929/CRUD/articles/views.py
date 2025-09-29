from django.shortcuts import render, redirect

# Create your views here.

from .models import Article

def index(request):
    # QuerySet API -> 전체데이터조회
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    # 단순 조회목적, GET방식이면 render
    # 생성, 수정, 삭제 POST방식이면 redirect
    return render(request, 'articles/index.html', context)

# 단일 게시글 페이지를 렌더링
def detail(request, pk):
    # QuerySet API -> 단일게시글조회 : get
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

# GET방식(단순히 페이지를 랜더링)
def new(request):
    return render(request, 'articles/new.html')

# POST방식(게시글 생성 - DB 저장)
def create(request):
    # form 태그의 name -> title, content
    # GET방식은 단순 조회 목적
    # ex) 데이터를 단순 조회하거나 검색
    # POST방식은 DB를 건든다.(보안과 관련)
    # ex) 데이터를 생성, 수정, 삭제 
    title = request.POST.get('title')
    content = request.POST.get('content')

    # ORM의 2번 방법(코드가 간결하면서도 안정성)
    # 안정성 : 데이터 관리(저장) 원칙
    # save()하기 전에 유효성 검사
    article = Article(title = title, content = content)
    article.save()

    # app_name = articles
    # name = detail
    return redirect('articles:detail', article.pk) 

# DB를 건든다. POST방식이다. -> redirect
def delete(request, pk):
    # 조회
    article = Article.objects.get(pk=pk)
    # 삭제
    article.delete()

    return redirect('articles:index')