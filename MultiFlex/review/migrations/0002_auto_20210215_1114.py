# Generated by Django 3.1.5 on 2021-02-15 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('video', '0001_initial'),
        ('review', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='video_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.video', verbose_name='영상'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
        migrations.AddField(
            model_name='comment',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.review'),
        ),
    ]
