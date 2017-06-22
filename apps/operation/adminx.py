# -*- encoding:utf-8 -*-
import xadmin
from .models import UserAsk, UserMessage, UserCourse, UserFavorite, CourseComments
__author__ = 'Amos'
__date__ = '2017/6/20 12:41'


class UserAskAdmin(object):
    """
    注册CityDict的管理器
    """
    list_display = ['name', 'phone', 'course_name', 'add_time']
    list_filter = ['name', 'phone', 'course_name', 'add_time']
    search_fields = ['name', 'phone', 'course_name']


class CourseCommentsAdmin(object):
    """
    创建CourseComments的管理器
    """
    list_display = ['user', 'course', 'comment', 'add_time']
    list_filter = ['user__nick_name', 'course__name', 'comment', 'add_time']
    search_fields = ['user__nick_name', 'course__name', 'comment']


class UserFavoriteAdmin(object):
    """
    创建UserFavorite的管理器
    """
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    list_filter = ['user__nick_name', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user__nick_name', 'fav_id', 'fav_type']


class UserCourseAdmin(object):
    """
    注册UserCourse的管理器
    """
    list_display = ['user', 'course', 'add_time']
    list_filter = ['user__nick_name', 'course__name', 'add_time']
    search_fields = ['user__nick_name', 'course__name']


class UserMessageAdmin(object):
    """
    注册 UserMessage的管理器
    """
    list_display = ['user', 'message', 'has_read', 'send_time']
    list_filter = ['user', 'message', 'has_read', 'send_time']
    search_fields = ['user', 'message', 'has_read']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)

