# Generated by Django 3.1.5 on 2021-02-02 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210202_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='bookmark',
        ),
    ]