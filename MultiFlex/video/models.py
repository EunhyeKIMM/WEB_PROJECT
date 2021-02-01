from django.db import models       # 모델추가를 위해 필수
from django.db.models.fields import CharField, IntegerField, PositiveIntegerField
# from taggit.managers import TaggableManager



# Create your models here.

# 영상
class Video(models.Model):

    VIDEO_TYPE_CHOICES = (
        ('movie', 'Movie'),
        ('drama', 'Drama')
    )

    VIDEO_GRADE_CHOICES = (
        ('all', "전체이용가"),
        ("12", "12세 이용가"),
        ("15", "15세 이용가"),
        ("19", "19세 이용가")
    )

    video_id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="제목", max_length=120),
    description = models.CharField(verbose_name="설명", max_length=500, null=True, help_text="영상 내용 설명")
    release_dt = models.DateField(verbose_name="개봉 일자", null=True)
    running_time = IntegerField(verbose_name="재생시간")
    director = CharField(verbose_name="제작자", max_length=100)
    video_type = CharField(verbose_name="영화/드라마 구분", max_length=50, choices=VIDEO_TYPE_CHOICES)
    recommend = PositiveIntegerField(verbose_name="추천수", default=0)
    grade = CharField(verbose_name="영상등급", max_length=50, choices=VIDEO_GRADE_CHOICES)
    # genre = TaggableManager(blank=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title