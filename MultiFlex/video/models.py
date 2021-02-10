from django.db import models
from django.urls import reverse
from user.models import *
from django.shortcuts import get_object_or_404
from taggit.managers import TaggableManager



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
    genre = TaggableManager(blank=True)
    running_time = models.PositiveIntegerField(verbose_name="재생시간")
    director = models.CharField(verbose_name="감독이름", max_length=30)
    video_type = models.CharField(verbose_name="구분", max_length=30, choices=VIDEO_TYPE)
    recommend = models.ManyToManyField(User, blank=True, related_name='like_user')
    grade = models.CharField(verbose_name="영화등급", max_length=30, choices=GRADE)
    video_link = models.URLField(verbose_name="VIDEO_URL", max_length=350)
    video_thumb = models.URLField(verbose_name="THUMBNAIL_URL", max_length=350)
    bookmark = models.ManyToManyField(User, blank=True, related_name='dibs_user')
    like = models.IntegerField(verbose_name="좋아요수", default=0)

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
        

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('video:video_detail', args=(self.video_id,))

    def count_like_user(self):
        return self.recommend.count()