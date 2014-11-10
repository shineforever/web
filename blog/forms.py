#! /usr/bin/env python
#! coding:utf-8
__author__ = 'shine_forever'

from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(label='姓名')
    email = forms.CharField(required=False,label='邮箱')
    content = forms.CharField(widget=forms.Textarea,label='内容')

