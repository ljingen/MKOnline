# -*- encoding:utf-8 -*-
from datetime import datetime
from django.db import models
from datetime import datetime

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
