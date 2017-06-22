# -*- encoding:utf-8 -*-
import xadmin
from  xadmin import views
from .models import EmailVerifyCode, Banner

__author__ = 'Amos'
__date__ = '2017/6/20 11:26'


class BaseSetting(object):
    """
    BaseSetting的作用是为了让后台的xadmin管理系统可以支持换主题，换背景
    """
    enable_themes = True  # 使用主题方案
    use_bootswatch = True  # 添加主题方案


class GlobalSettings(object):
    site_title = "后台管理系统"
    site_footer = "米米公社"
    menu_style = "accordion"


class EmailVerifyCodeAdmin(object):
    """
    注册EmailVerifyCode的管理器
    """
    list_display = ['code', 'email', 'send_type', 'send_time']
    list_filter = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']


class BannerAdmin(object):
    """
    注册Banner的管理器
    """
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']

xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(EmailVerifyCode, EmailVerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

