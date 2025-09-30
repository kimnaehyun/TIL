from django.db import models
# AbstractUser가 로그인, 권한관리 등에 필요한 기본적인 필드 제공
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
