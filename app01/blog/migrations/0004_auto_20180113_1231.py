# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180113_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='first_name',
            field=models.CharField(default=datetime.datetime(2018, 1, 13, 4, 31, 32, 635000, tzinfo=utc), max_length=50, verbose_name='\u59d3'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(default=datetime.datetime(2018, 1, 13, 4, 31, 53, 56000, tzinfo=utc), max_length=50, verbose_name='\u540d'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, verbose_name='\u6807\u7b7e'),
        ),
    ]
