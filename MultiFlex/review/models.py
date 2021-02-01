# Create your models here.
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField, PositiveIntegerField
from django.db.models.fields.related import ForeignKey
from tinymce.models import HTMLField


# from user.models import MTF_User

# Create your models here.
class Review(models.Model):
    re_id = models.AutoField(verbose_name="리뷰등록번호", primary_key=True)
    re_title = models.CharField(verbose_name="리뷰 제목", max_length=120)
    content = HTMLField('CONTENT')
    create_dt = DateField(verbose_name="작성일자", auto_now_add=True)
    modify_dt = DateField(verbose_name="수정일자", auto_now=True)
    # user_id = ForeignKey(MTF_User, verbose_name="작성자", on_delete=models.CASCADE)
    # re_video_id = ForeignKey('Video', verbose_name="영상 제목", on_delete=models.CASCADE)
    like = PositiveIntegerField(verbose_name="좋아요", default=0)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title