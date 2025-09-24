from django.db import models

# Create your models here.
class Article(models.Model):
    # 글자 제한이 최대 20자인 title 필드
    title = models.CharField(max_length=20)
    # 글자 제한이 없는 텍스트 필드
    context = models.TextField()
    # 객체가 처음 생성 될 때 시간이 자동으로 추가 (auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # 객체가 저장 될 때마다 현재 시간 자동 업데이트 (auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
