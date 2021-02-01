from django.db import models       # 모델추가를 위해 필수
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):

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
    email = models.EmailField(verbose_name="email", unique=True)
    name = models.CharField(verbose_name="이름", max_length=150)
    joined_dt = models.DateTimeField(verbose_name="가입일자", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="최근 로그인 일자", auto_now=True)
    bookmark = models.ForeignKey(Review, verbose_name="찜한 목록", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, verbose_name='활성화 여부')
    is_admin = models.BooleanField(default=False, verbose_name='관리자 여부')
    pass

class UserManager(BaseUserManager):
    def _create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('이메일은 필수입니다.')
    
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)     # 패스워드 암호화
        user.save(using=self._db)
 
    def create_user(self, email, password, **kwargs):
        """
        일반 유저 생성
        """
        kwargs.setdefault('is_admin', False)
        return self._create_user(email, password, **kwargs)
 
    def create_superuser(self, email, password, **kwargs):
        """
        관리자 유저 생성
        """
        kwargs.setdefault('is_admin', True)
        return self._create_user(email, password, **kwargs)


class Review(models.Model):
    re_id = models.IntegerField(verbose_name="리뷰등록번호", primary_key=True)
    pass








class Video(models.Model):
    video_id = models.IntegerField(verbose_name="#", primary_key=True)
    pass


