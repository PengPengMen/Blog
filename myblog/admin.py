# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Post, Category, Tag
from django.contrib import admin

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

# 把新增的 PostAdmin 也注册进来
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)