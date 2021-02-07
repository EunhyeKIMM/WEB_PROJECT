# Generated by Django 3.1.5 on 2021-02-07 13:42

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('video', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('re_title', models.CharField(max_length=100, verbose_name='리뷰 제목')),
                ('content', tinymce.models.HTMLField(verbose_name='CONTENT')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='작성일자')),
                ('modify_dt', models.DateTimeField(auto_now=True, verbose_name='수정일자')),
                ('like', models.PositiveIntegerField(default=0, verbose_name='좋아요')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='작성자')),
                ('video_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.video', verbose_name='영상')),
            ],
        ),
    ]
