from django.db import models

# Create your models here.

class Review(models.Model):
    re_id = models.IntegerField(verbose_name="리뷰등록번호", primary_key=True)
    pass