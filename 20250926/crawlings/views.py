from django.shortcuts import render, redirect, get_object_or_404
from .models import Crawling

def index(request):
    return render(request, 'crawlings/index.html')

def search(request):
    company = request.GET.get('company')
    crawling = Crawling.objects.filter(company_name=company) if company else []
    context = {
        'crawling': crawling,
        'company': company
    }
    return render(request, 'crawlings/index.html', context)

def delete(request, pk):
    crawling = Crawling.objects.get(pk=pk)
    company = crawling.company_name  # 삭제 후 같은 회사 검색 결과로 돌아가기 위해 저장
    crawling.delete()
    return redirect(f'/crawlings/search/?company={company}')
