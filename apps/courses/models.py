# -*- encoding:utf-8 -*-
from datetime import datetime
from django.db import models

# Create your models here.


class Course(models.Model):
    """
    课程详细字段信息
    """
    name = models.CharField(max_length=100, verbose_name=u'课程名')
    desc = models.CharField(max_length=300, verbose_name=u'课程简介')
    detail = models.TextField(verbose_name=u'课程详情')
    degree = models.CharField(max_length=5, choices=((u'gj', u'高级'), (u'zj', u'中级'), (u'cj', u'低级')),
                              verbose_name=u'难度')
    image = models.ImageField(max_length=100, upload_to='courses/%Y/%m', default='image/default.png',
                              verbose_name=u'封面图')
    learn_times = models.IntegerField(default=0, verbose_name=u'学习时长(分钟)')
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """
    课程里面的具体张杰
    """
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name=u'章节名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(models.Model):
    """
    课程里面的具体视频
    """
    lesson = models.ForeignKey(Lesson, verbose_name=u'章节')
    name = models.CharField(max_length=100, verbose_name=u'视频名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    """
    课程资源表
    """
    course = models.ForeignKey(Course, verbose_name=u'课程')
    name = models.CharField(max_length=50, verbose_name=u'资源名称')
    download = models.FileField(upload_to='course/resource/%Y/%m', verbose_name='资源文件', max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程资料'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
