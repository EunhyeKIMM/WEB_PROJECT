from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from video.models import *

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password, age, gender, phone, username, **kwargs):
        """
        일반 유저 생성
        """
        if not email:
            raise ValueError('이메일은 필수입니다.')
    
        user = self.model(
            email=self.normalize_email(email),
            age = age,
            gender = gender,
            phone = phone,
            username = username,
            **kwargs
        )
        user.set_password(password)     # 패스워드 암호화
        user.save(using=self._db)

        return user
 
    def create_superuser(self, email, password, age, gender, phone, username, **kwargs):
        """
        관리자 유저 생성
        """
        if not email:
            raise ValueError('이메일은 필수입니다.')
    
        user = self.model(
            email=self.normalize_email(email),
            age = age,
            gender = gender,
            phone = phone,
            username = username,
            **kwargs
        )
        user.is_admin = True
        user.set_password(password)     # 패스워드 암호화
        user.save(using=self._db)
        
        return user

class User(AbstractBaseUser):

    GENDER = (
        ("male", "남성"),
        ("female", "여성")
    )

    email = models.EmailField(verbose_name="이메일", max_length=128, unique=True)
    password = models.CharField(verbose_name="PWD", max_length=128)
    age = models.PositiveIntegerField(verbose_name="나이")
    gender = models.CharField(verbose_name="성별", max_length=10, choices=GENDER)
    phone = models.CharField(verbose_name="전화번호", max_length=13)
    username = models.CharField(verbose_name="이름", max_length=30)
    joined_dt = models.DateField(verbose_name="가입일자", auto_now_add=True)
    last_login = models.DateField(verbose_name="최근 로그인 일자", auto_now=True)
    is_active = models.BooleanField(default=True, verbose_name='ID 활성화 여부')
    is_admin = models.BooleanField(default=False, verbose_name='관리자 여부')
    is_staff = models.BooleanField(default=False, verbose_name="직원 여부")
    
    
    # 모델 매니저
    objects = UserManager()

    # 필수 목록
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'age', 'gender', 'phone', 'username']

    class Meta:
        db_table = 'user'
        verbose_name = '유저'
        verbose_name_plural = '유저들'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin