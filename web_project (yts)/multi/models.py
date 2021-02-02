from django.db import models

# Create your models here.
class Video(models.Model):
    video_id = models.IntegerField(primary_key=True)
    title = models.CharField(verbose_name="제목", max_length=120),
    description = models.CharField(verbose_name="설명", max_length=500, null=True, help_text="영상 내용 설명")

    def __str__(self):
        pass

class User(models.Model):
    user_id = models.CharField(verbose_name="ID", max_length=20, primary_key=True)
    password = models.CharField(verbose_name="PWD",max_length=128)
    age = models.PositiveIntegerField(verbose_name="나이")
    gender = models.CharField(verbose_name="성별", max_length=50, )
    bookmark = models.ForeignKey(Video,on_delete=models.CASCADE)

    def __str__(self):
        pass

class Review(models.Model):
    re_id = models.AutoField(verbose_name="리뷰등록번호", primary_key=True)
    re_title = models.CharField(verbose_name="리뷰 제목", max_length=120)
    user_review = models.ForeignKey(User,verbose_name="작성자",on_delete=models.CASCADE,null=True)#작성자
    #content = HTMLField('CONTENT')

    def __str__(self):
        pass