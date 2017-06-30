# -*- encoding:utf-8 -*-
from datetime import datetime, timezone
from django.db import models
from datetime import datetime

from users.models import UserProfile

# Create your models here.


class CityDict(models.Model):
    """
    城市字典表
    """
    name = models.CharField(max_length=30, verbose_name=u'城市名')
    desc = models.CharField(max_length=100, verbose_name=u'简介')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(models.Model):
    """
    课程机构表
    """
    name = models.CharField(max_length=50, verbose_name=u'机构名称')
    desc = models.TextField(verbose_name=u'机构介绍')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    category = models.CharField('类别', choices=(('pxjg', u'培训机构'), ('gx', u'高校'), ('gr', u'个人')), default='pxjg', max_length=5)
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏数')
    address = models.CharField(max_length=100, verbose_name=u'机构地址')
    city = models.ForeignKey(CityDict, verbose_name=u'城市')
    image = models.ImageField(max_length=100, upload_to='org/%Y/%m',
                              default='image/default.png', verbose_name=u'封面图')
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    course_nums = models.IntegerField(default=0, verbose_name=u'课程数')

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')



    class Meta:
        verbose_name = u'机构'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(models.Model):
    """
    教师表
    """
    org = models.ForeignKey(CourseOrg, verbose_name=u'所属机构')
    name = models.CharField(max_length=30, verbose_name=u'教师名')
    image = models.ImageField(max_length=100, upload_to='image/%Y/%m',
                              default='image/default.png', verbose_name=u'头像')
    work_years = models.IntegerField(default=0, verbose_name=u'工作年限')
    work_company = models.CharField(max_length=50, verbose_name=u'就职公司')
    work_position = models.CharField(max_length=30, verbose_name=u'公司职位')
    point = models.CharField(max_length=100, verbose_name=u'教学特点')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'教师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    分类表
    """
    name = models.CharField(max_length=40, verbose_name=u'类别')

    class Meta:
        verbose_name = u'分类表'
        verbose_name_plural = verbose_name


class Equipment(models.Model):
    """
    设备表
    """
    name = models.CharField(max_length=40, verbose_name=u'设备名')
    category = models.ForeignKey(Category, verbose_name=u'类别')

    class Meta:
        verbose_name = u'设备'
        verbose_name_plural = verbose_name


class Characteristic(models.Model):
    """
    设备参数
    """
    category = models.ForeignKey(Category, verbose_name=u'类别')
    name = models.CharField(max_length=40, verbose_name=u'设备参数')

    class Meta:
        verbose_name = u'设备参数'
        verbose_name_plural = verbose_name


class CharacteristicValue(models.Model):
    """
    设备参数的值的数据结构:
    """
    equipment = models.ForeignKey(Equipment, verbose_name=u'设备')
    characteristic = models.ForeignKey(Characteristic, verbose_name=u'特性')
    value = models.CharField(max_length=100, verbose_name=u'设备参数值')


class Blog(models.Model):
    """
    文章Blog
    """
    STATUS_CHOICES = (
        ('draft', u'草稿'),
        ('published', u'发布'),
    )
    author = models.ForeignKey(UserProfile, verbose_name=u'作者')
    title = models.CharField(u'标题', max_length=50)
    body = models.TextField(u'正文')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    publish = models.DateTimeField(default=datetime.now, verbose_name=u'发布时间')
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name=u'状态')

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = verbose_name


class BlogContent(models.Model):
    blog = models.ForeignKey(Blog, verbose_name=u'文章')
    author = models.ForeignKey(UserProfile, verbose_name=u'作者')
    contents = models.TextField(u'内容', max_length=2000)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'评论时间')
    add_time = models.TimeField(auto_now_add=True, verbose_name=u'添加时间')
    add_date = models.DateField(auto_now_add=True, verbose_name=u'添加日期')

    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = verbose_name
