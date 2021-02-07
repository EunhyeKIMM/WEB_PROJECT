from django.db import models

# Create your models here.

class User(models.Model):

    GENDER = (
        ("male", "남성"),
        ("female", "여성")
    )

    email = models.EmailField(verbose_name="이메일", max_length=128, unique=True)
    password = models.CharField(verbose_name="PWD", max_length=128)
    age = models.PositiveIntegerField(verbose_name="나이")
    gender = models.CharField(verbose_name="성별", max_length=10, choices=GENDER)
    phone = models.CharField(verbose_name="전화번호", max_length=13)
    name = models.CharField(verbose_name="이름", max_length=30)
    joined_dt = models.DateField(verbose_name="가입일자", auto_now_add=True)
    last_login = models.DateField(verbose_name="최근 로그인 일자", auto_now=True)
    is_active = models.BooleanField(default=True, verbose_name='ID 활성화 여부')
    is_admin = models.BooleanField(default=False, verbose_name='관리자 여부')
    is_staff = models.BooleanField(default=False, verbose_name="직원 여부")
    bookmark = models.CharField(verbose_name="찜한 영상", max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.email

    class Meta:
        db_table = 'user'



# Create your models here.
# class UserManager(BaseUserManager):
#     def _create_user(self, email, password, age, gender, phone, name, **kwargs):
#         if not email:
#             raise ValueError('이메일은 필수입니다.')
    
#         user = self.model(
#             email=self.normalize_email(email),
#             age = age, 
#             gender = gender,
#             phone = phone,
#             name = name,
#             **kwargs
#         )
#         user.set_password(password)     # 패스워드 암호화
#         user.save(using=self._db)
    
#     def create_user(self, email, password, age, gender, phone, name, **kwargs):
#         """
#         일반 유저 생성
#         """
#         kwargs.setdefault('is_admin', False)
#         return self._create_user(email, password, age, gender, phone, name, **kwargs)
 
#     def create_superuser(self, email, password, age, gender, phone, name, **kwargs):
#         """
#         관리자 유저 생성
#         """
#         kwargs.setdefault('is_admin', True)
#         return self._create_user(email, password, age, gender, phone, name, **kwargs)


# class User(AbstractBaseUser): # 사용자 ID로 email을 사용

#     GENDER = (
#         ("male", "남성"),
#         ("female", "여성")
#     )

#     email = models.EmailField(unique=True, verbose_name='이메일')
#     password = models.CharField(verbose_name="PWD", max_length=128)
#     age = models.PositiveIntegerField(verbose_name="나이")
#     gender = models.CharField(verbose_name="성별", max_length=10, choices=GENDER)
#     phone = models.CharField(verbose_name="연락처", max_length=20)
#     name = models.CharField(max_length=20, verbose_name='이름')
#     date_joined = models.DateTimeField(auto_now_add=True, verbose_name='가입일')
#     is_active = models.BooleanField(default=True, verbose_name='활성화 여부')
#     is_admin = models.BooleanField(default=False, verbose_name='관리자 여부')
#     last_login = models.DateTimeField(verbose_name="최근 로그인 일자", auto_now=True)
#     is_staff = models.BooleanField(default=False, verbose_name="직원 여부")
#     bookmark = models.CharField(verbose_name="찜한 영상", max_length=50, null=True, blank=True)


#     # 모델 매니저
#     objects = UserManager()

#     # 필수 목록
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['password', 'age', 'gender', 'phone', 'name']

#     class Meta:
#         db_table = 'user'
#         verbose_name = '유저'
#         verbose_name_plural = '유저들'

#     @property
#     def is_superuser(self):
#         return self.is_admin

#     @property
#     def is_staff(self):
#         return self.is_admin

#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     def has_module_perms(self, app_label):
#         return self.is_admin

#     @is_staff.setter
#     def is_staff(self, value):
#         self._is_staff = value
