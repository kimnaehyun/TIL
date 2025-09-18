from django.shortcuts import render

# Create your views here.
def index(request): 
    # index.html 파일 페이지를 랜더링하겠다.
    return render(request, 'articles/index.html')