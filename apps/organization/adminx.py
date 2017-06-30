# -*- encoding:utf-8 -*-
import xadmin
from .models import CityDict, CourseOrg, Teacher, Blog, BlogContent
__author__ = 'Amos'
__date__ = '2017/6/20 11:48'


class CityDictAdmin(object):
    """
    注册CityDict的管理器
    """
    list_display = ['name', 'desc', 'add_time']
    list_filter = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']


class CourseOrgAdmin(object):
    """
    注册LessonAdmin的管理器
    """
    list_display = ['name', 'city', 'click_nums', 'fav_nums', 'address',  'image', 'add_time']
    list_filter = ['name',  'city', 'click_nums', 'fav_nums', 'address',  'image', 'add_time']
    search_fields = ['name',  'city', 'click_nums', 'fav_nums', 'address',  'image']


class TeacherAdmin(object):
    """
    注册Video的管理器
    """
    list_display = ['org', 'name', 'image', 'work_years', 'work_company', 'add_time']
    list_filter = ['org', 'name', 'image', 'work_years', 'work_company', 'add_time']
    search_fields = ['org', 'name', 'image', 'work_years', 'work_company']


class BlogAdmin(object):
    """
    注册Blog的管理器
    """
    list_display = ['author', 'title', 'body', 'add_time', 'status']
    list_filter = ['author', 'title', 'body', 'add_time', 'status']
    search_fields = ['author', 'title', 'body', 'status']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(Blog, BlogAdmin)
