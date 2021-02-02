# Generated by Django 3.1.5 on 2021-02-02 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('video_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120, verbose_name='영상 제목')),
                ('description', models.CharField(max_length=500, null=True, verbose_name='설명')),
                ('release_dt', models.DateField(null=True, verbose_name='개봉일자')),
                ('genre', models.CharField(max_length=30, null=True, verbose_name='장르')),
                ('running_time', models.PositiveIntegerField(verbose_name='재생시간')),
                ('director', models.CharField(max_length=30, verbose_name='감독이름')),
                ('video_type', models.CharField(choices=[('movie', '영화'), ('drama', '드라마')], max_length=30, verbose_name='구분')),
                ('recommend', models.PositiveIntegerField(default=0, verbose_name='추천수')),
                ('grade', models.CharField(choices=[('all', '전체관람'), ('12', '12세이용'), ('15', '15세이용'), ('19', '19세이용')], max_length=30, verbose_name='영화등급')),
            ],
        ),
    ]
