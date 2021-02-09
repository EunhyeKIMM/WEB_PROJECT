

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('video_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120, verbose_name='영상 제목')),
                ('description', models.CharField(max_length=500, null=True, verbose_name='설명')),
                ('release_dt', models.DateField(null=True, verbose_name='개봉일자')),
                ('running_time', models.PositiveIntegerField(verbose_name='재생시간')),
                ('director', models.CharField(max_length=30, verbose_name='감독이름')),
                ('video_type', models.CharField(choices=[('movie', '영화'), ('drama', '드라마')], max_length=30, verbose_name='구분')),
                ('recommend', models.PositiveIntegerField(default=0, verbose_name='추천수')),
                ('grade', models.CharField(choices=[('all', '전체관람'), ('12', '12세이용'), ('15', '15세이용'), ('19', '19세이용')], max_length=30, verbose_name='영화등급')),
                ('video_link', models.URLField(max_length=350, verbose_name='VIDEO_URL')),
                ('video_thumb', models.URLField(max_length=350, verbose_name='THUMBNAIL_URL')),
                ('genre', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'video',
                'verbose_name_plural': 'videos',
            },
        ),
    ]
