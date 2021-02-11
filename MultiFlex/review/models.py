from video.models import Video
from django.db import models
from tinymce.models import HTMLField
from user.models import User
from django.urls import reverse
# Create your models here.

class Review(models.Model):
    re_title = models.CharField(verbose_name="TITLE", max_length=100)
    content = HTMLField('CONTENT')
    create_dt = models.DateTimeField(verbose_name="작성일자", auto_now_add=True)
    modify_dt = models.DateTimeField(verbose_name="수정일자", auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="작성자")
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE, verbose_name="영상")
    like = models.PositiveIntegerField(verbose_name="좋아요", default=0)
    read_cnt = models.IntegerField(default=0)

    def __str__(self):
        return self.re_title

    def get_absolute_url(self):
        return reverse('/video/<int:pk>/video_detail/', args=(self.video_id,))

class Comment(models.Model):
    document = models.ForeignKey(Review,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, verbose_name="작성자")
    text = models.TextField()
    create_dt = models.DateTimeField(verbose_name="작성일자", auto_now_add=True)
    modify_dt = models.DateTimeField(verbose_name="수정일자", auto_now=True)
