# -*- encoding:utf-8 -*-
import xadmin
from .models import Course, Lesson, Video, CourseResource
__author__ = 'Amos'
__date__ = '2017/6/20 11:48'


class CourseAdmin(object):
    """
    注册Course的管理器
    """
    list_display = ['name', 'desc', 'degree', 'image', 'learn_times', 'students', 'fav_nums', 'click_nums', 'add_time']
    list_filter = ['name', 'desc', 'degree', 'image', 'learn_times', 'students', 'fav_nums', 'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'image', 'learn_times', 'students', 'fav_nums', 'click_nums']


class LessonAdmin(object):
    """
    注册LessonAdmin的管理器
    """
    list_display = ['course', 'name', 'add_time']
    list_filter = ['course__name', 'name']
    search_fields = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    """
    注册Video的管理器
    """
    list_display = ['lesson', 'name', 'add_time']
    list_filter = ['lesson__name', 'name']
    search_fields = ['lesson__name', 'name', 'add_time']


class CourseResourceAdmin(object):
    """
    注册CourseResource的管理器
    """
    list_display = ['course', 'name', 'download', 'add_time']
    list_filter = ['course__name', 'name', 'download']
    search_fields = ['course__name', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)