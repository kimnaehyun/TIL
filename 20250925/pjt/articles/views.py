from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    # QuerySet API -> 전체데이터조회
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    # 단순 조회 목적, GET방식이면 render
    # 생성, 수정, 삭제 POST방식이면 redirect
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    # QuerySet API -> 단일 게시글 조회 : get
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request,'articles/detail.html', context)