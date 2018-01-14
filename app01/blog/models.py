# -*- encoding: UTF-8 -*-

from django.db import models
from django.contrib import admin
# Create your models here.

class Author(models.Model):
    """
    作者
    """
    first_name = models.CharField(u'姓',max_length=50)
    last_name = models.CharField(u'名',max_length=50)
    def my_property(self):
        return self.first_name + ' ' + self.last_name

    my_property.short_description = "真实名称"
    full_name = property(my_property)

    name = models.CharField(u'作者名称',max_length=50)
    qq = models.CharField(u'QQ',max_length=10)
    addr = models.TextField(u'地址')
    email = models.EmailField(u'邮箱')
    pub_time = models.DateTimeField(u'添加时间',auto_now_add=True,editable=True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True,null=True)

    def __unicode__(self):
        return self.name

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name','name','qq','addr','email','pub_time','update_time')


class Article(models.Model):
    title = models.CharField(u'标题',max_length=50)
    # 作者外键
    author = models.ForeignKey(Author)
    content = models.TextField(u'内容')
    score = models.IntegerField(u'评分')
    tags = models.ManyToManyField('Tag')
    pub_time = models.DateTimeField(u'添加时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    def __unicode__(self):
        return self.title

class ArticleAdmin(admin.ModelAdmin):
    # def get_queryset(self, request):
    #     qs = super(ArticleAdmin,self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     else:
    #         return qs.filter(author=request.user)
    #列表显示字段
    list_display = ('title','author','score','pub_time','update_time',)
    #搜索字段
    search_fields = ('title',)

    list_filter = ('author',)

    fieldsets = (
        ('基础信息', {'fields': (('title', 'author'), 'score')}),
        ('详细信息', {
            'classes':('extrapretty'),
            'fields': ('content',)
        }),
    )

class Tag(models.Model):
    name = models.CharField(u'标签',max_length=50)

    def __unicode__(self):
        return self.name
