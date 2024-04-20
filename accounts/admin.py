from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
# 대체하기 3단계 : admin 사이트에 새로운 user 모델 등록
admin.site.register(User, UserAdmin)