# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='pub_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 13, 4, 20, 9, 88000, tzinfo=utc), verbose_name='\u6dfb\u52a0\u65f6\u95f4', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='\u5185\u5bb9'),
        ),
        migrations.AlterField(
            model_name='article',
            name='score',
            field=models.IntegerField(verbose_name='\u8bc4\u5206'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50, verbose_name='\u6807\u9898'),
        ),
        migrations.AlterField(
            model_name='author',
            name='addr',
            field=models.TextField(verbose_name='\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='\u90ae\u7bb1'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=50, verbose_name='\u4f5c\u8005\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='author',
            name='qq',
            field=models.CharField(max_length=10, verbose_name='QQ'),
        ),
    ]
