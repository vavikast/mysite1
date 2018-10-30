# -*- coding: utf-8 -*-
2018 - 10 - 30
__author__ = 'Felix'

from  django import forms

class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128)
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput)