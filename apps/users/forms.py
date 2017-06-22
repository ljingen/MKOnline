# -*- encoding:utf-8 -*-
from django import forms
from captcha.fields import CaptchaField

__author__ = 'Amos'
__date__ = '2017/6/21 15:12'


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(min_length=6, required=True)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(required=True, min_length=5)
    password1 = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})
