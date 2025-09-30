from django.shortcuts import render
# auth는 Model Form을 안 쓴다.
# built-in form 사용
from django.contrib.auth.forms import (
    AuthenticationForm # 로그인을 위한 폼
)
from django.contrib.auth import login as auth_login

def login(request):
    pass