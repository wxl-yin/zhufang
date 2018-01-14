# -*— encoding: utf-8 -*-
from django.db import models

# Create your models here.

class Person(models.Model):
    # 名称
    name = models.CharField(max_length=20)
    # 年龄
    age = models.IntegerField()

    def __unicode__(self):
        return self.name


class Blog(models.Model):
    """
    博客
    """
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __unicode__(self):  # __str__ on Python 3
        return self.name


class Author(models.Model):
    """
    作者
    """
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __unicode__(self):  # __str__ on Python 3
        return self.name

class Entry(models.Model):
    """
    条目
    """
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __unicode__(self):  # __str__ on Python 3
        return self.headline