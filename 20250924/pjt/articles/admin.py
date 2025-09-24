from django.contrib import admin
from .models import Article
# Register your models here.
# 관리자 페이지에 Article 모델을 등록하겠다.
admin.site.register(Article)