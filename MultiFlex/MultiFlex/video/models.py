from django.db import models

# Create your models here.

class Video(models.Model):
    video_id = models.IntegerField(verbose_name="#", primary_key=True)
    pass