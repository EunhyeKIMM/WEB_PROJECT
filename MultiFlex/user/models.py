from django.db import models


# Create your models here.

class User(models.Model):

    GENDER = (
        ("male", "남성"),
        ("female", "여성")
    )

    user_id = models.CharField(verbose_name="ID", max_length=50)
    password = models.CharField(verbose_name="PWD", max_length=128)
    age = models.PositiveIntegerField(verbose_name="나이")
    gender = models.CharField(verbose_name="성별", max_length=10, choices=GENDER)
    phone = models.CharField(verbose_name="전화번호", max_length=13)
    email = models.EmailField(verbose_name="이메일")
    name = models.CharField(verbose_name="이름", max_length=30)
    joined_dt = models.DateField(verbose_name="가입일자", auto_now_add=True)
    last_login = models.DateField(verbose_name="최근 로그인 일자", auto_now=True)
    is_active = models.BooleanField(default=True, verbose_name='ID 활성화 여부')
    is_admin = models.BooleanField(default=False, verbose_name='관리자 여부')
    is_staff = models.BooleanField(default=False, verbose_name="직원 여부")
    bookmark = models.CharField(verbose_name="찜한 영상", max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.user_id