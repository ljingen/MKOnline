# -*- encoding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.


class UserProfile(AbstractUser):
    """
    用户信息表，继承自AbstractUser
    """
    GENDER_CHOICES = (
        (u'MALE', u'男'),
        (u'FEMALE', u'女'),
    )
    nick_name = models.CharField(max_length=30, verbose_name=u'昵称', default='')
    birthday = models.DateField(default=datetime.now, verbose_name=u'生日')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='MALE', verbose_name=u'性别')
    address = models.CharField(max_length=100, default='', verbose_name=u'地址')
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name=u'手机号')
    email = models.EmailField(max_length=100, default='', verbose_name=u'邮箱')
    image = models.ImageField(max_length=100, upload_to='images/%Y/%m', default='/image/default.png', verbose_name=u'用户头像')

    class Meta:
        verbose_name = u'用户资料'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyCode(models.Model):
    code = models.CharField(max_length=16, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u'发送时间')
    send_type = models.IntegerField(choices=((1, '注册'), (2, '忘记密码')), default=1, verbose_name=u'发送类型')

    class Meta:
        verbose_name = u'验证码'
        verbose_name_plural = verbose_name


class Banner(models.Model):
    """
    首页的banner导航，三个变量
    """
    title = models.CharField(max_length=100, verbose_name=u'标题')
    image = models.ImageField(max_length=100, upload_to='images/%Y/%m', verbose_name=u'封面')
    url = models.URLField(max_length=200, verbose_name=u'访问地址')
    index = models.IntegerField(default=100, verbose_name=u'顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name
