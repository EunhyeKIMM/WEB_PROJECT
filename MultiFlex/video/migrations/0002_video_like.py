# Generated by Django 3.1.5 on 2021-02-10 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='like',
            field=models.IntegerField(default=0, verbose_name='좋아요수'),
        ),
    ]