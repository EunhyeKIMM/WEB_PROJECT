from django.db import models


# Create your models here.

class Video(models.Model):

    VIDEO_TYPE = (
        ("movie", "영화"),
        ("drama", "드라마")
    )

    GRADE = (
        ("all","전체관람"),
        ("12","12세이용"),
        ("15","15세이용"),
        ("19","19세이용")
    )

    video_id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="영상 제목", max_length=120)
    description = models.CharField(verbose_name="설명", max_length=500, null=True)
    release_dt = models.DateField(verbose_name="개봉일자", null=True)
    genre = models.CharField(verbose_name="장르", max_length=30, null=True)
    running_time = models.PositiveIntegerField(verbose_name="재생시간")
    director = models.CharField(verbose_name="감독이름", max_length=30)
    video_type = models.CharField(verbose_name="구분", max_length=30, choices=VIDEO_TYPE)
    recommend = models.PositiveIntegerField(verbose_name="추천수", default=0)
    grade = models.CharField(verbose_name="영화등급", max_length=30, choices=GRADE)
    video_link = models.URLField(verbose_name="URL", max_length=350)

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
        

    def __str__(self):
        return self.title