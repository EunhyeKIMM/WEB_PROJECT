from review.models import Review
from django.db import models       # 모델추가를 위해 필수

# Create your models here.

class User(models.Model):

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified', 'Not Specified')
    )

    user_id = models.CharField(verbose_name="ID", max_length=20, primary_key=True)
    password = models.CharField(verbose_name="PWD", max_length=128)
    age = models.PositiveIntegerField(verbose_name="나이")              # 나이이므로 음수 불가
    gender = models.CharField(verbose_name="성별", max_length=50, choices=GENDER_CHOICES)
    phone_number = models.CharField(verbose_name="연락처", max_length=120)
    email = models.EmailField(verbose_name="email")
    name = models.CharField(verbose_name="이름", max_length=150)
    joined_dt = models.DateTimeField(verbose_name="가입일자", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="최근 로그인 일자", auto_now=True)
    bookmark = models.ForeignKey(Review, verbose_name="찜한 목록", on_delete=models.CASCADE)
    pass