# -*- coding: UTF-8 -*-
from django.db import models

# Create your models here.
import sys
default__concoding = 'utf-8'

class Room(models.Model):
    """
    定义一个人类
    """
    # 开发商家
    seller = models.CharField(max_length=30)
    room_num = models.IntegerField()

    def __unicode__(self):
        # 在Python3中使用 def __str__(self):
        return self.seller.encode("UTF-8")