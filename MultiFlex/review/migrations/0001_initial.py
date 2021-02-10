# Generated by Django 3.1.5 on 2021-02-09 21:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('re_title', models.CharField(max_length=100, verbose_name='TITLE')),
                ('content', tinymce.models.HTMLField(verbose_name='CONTENT')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='작성일자')),
                ('modify_dt', models.DateTimeField(auto_now=True, verbose_name='수정일자')),
                ('like', models.PositiveIntegerField(default=0, verbose_name='좋아요')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
    ]
