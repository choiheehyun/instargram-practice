from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 대체하기 1단계 : AbstractUser를 상속받는 새로운 User 클래스 정의
class User(AbstractUser):
    pass