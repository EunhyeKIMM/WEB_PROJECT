# Generated by Django 3.1.5 on 2021-02-11 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=30, verbose_name='TEXT'),
        ),
    ]
