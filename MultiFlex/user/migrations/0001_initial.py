# Generated by Django 3.1.5 on 2021-02-10 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=128, unique=True, verbose_name='이메일')),
                ('password', models.CharField(max_length=128, verbose_name='PWD')),
                ('age', models.PositiveIntegerField(verbose_name='나이')),
                ('gender', models.CharField(choices=[('male', '남성'), ('female', '여성')], max_length=10, verbose_name='성별')),
                ('phone', models.CharField(max_length=13, verbose_name='전화번호')),
                ('username', models.CharField(max_length=30, verbose_name='이름')),
                ('joined_dt', models.DateField(auto_now_add=True, verbose_name='가입일자')),
                ('last_login', models.DateField(auto_now=True, verbose_name='최근 로그인 일자')),
                ('is_active', models.BooleanField(default=True, verbose_name='ID 활성화 여부')),
                ('is_admin', models.BooleanField(default=False, verbose_name='관리자 여부')),
            ],
            options={
                'verbose_name': '유저',
                'verbose_name_plural': '유저들',
                'db_table': 'user',
            },
        ),
    ]
