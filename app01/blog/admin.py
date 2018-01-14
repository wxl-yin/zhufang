# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Article,ArticleAdmin)

admin.site.register(Author,AuthorAdmin)

admin.site.register(Tag)