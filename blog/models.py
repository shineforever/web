#coding:utf-8
from django.db import models
from django.contrib import admin
from DjangoUeditor.modeles import UEditorField
import time




# Create your models here.
#文章分类
class Category(models.Model):
    name = models.CharField(max_length=100)
    article_num = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % self.name


#文章
class Article(models.Model):
    category = models.ForeignKey(Category)
    caption = models.CharField(max_length=200)    #标题
    shortcontent = models.TextField(max_length=500)
    content = UEditorField('contexnt')
    createtime = models.DateTimeField(auto_now_add=True)
    hits = models.IntegerField(default=0)
    times = models.IntegerField(default=0)
    goods = models.IntegerField(default=0)
    bads = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % self.caption


#评论
class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    createtime = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article)

    def __unicode__(self):
        return u'%s' % self.article


