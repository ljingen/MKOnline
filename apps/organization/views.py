# -*- encoding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from MXonline.settings import MEDIA_ROOT
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
import json
from .models import CityDict, CourseOrg

# Create your views here.


class CourseOrgView(View):
    """
    get:返回当前的机构清单
    """
    def get(self, request):
        category = request.GET.get('ct', '')
        city_id = request.GET.get('city', '')
        sort = request.GET.get('sort','')
        # 获取到所有的城市
        all_citys = CityDict.objects.all()
        all_orgs = CourseOrg.objects.all()
        '''获取到授课机构排名前五位'''
        hot_orgs = all_orgs.order_by('-click_nums')[:5]

        '''获取到所有的机构列表,并根据类别进行过滤'''
        if category:
            all_orgs = all_orgs.filter(category=category)
        '''按照城市进行筛选'''
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))
        '''按照类别进行排序筛选'''
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by('-students')
            elif sort =='courses':
                all_orgs = all_orgs.order_by('-course_nums')
        '''获取到当前的机构数量'''
        count = all_orgs.count()
        '''翻页的处理'''
        try:
            page = request.GET.get('page', 1)  # 获取页面，默认为第一页
        except PageNotAnInteger:
            page = 1  # 如果没有获取到，则设置为默认第一页

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_orgs, 3, request=request)

        # 处理之后的list清单
        all_orgs = p.page(page)

        return render(request, 'org-list.html', {'all_citys': all_citys,  # 返回所有城市信息
                                                 'all_orgs': all_orgs,  # 返回所有筛选或排序的机构
                                                 'category': category,  # 返回机构类别信息到html里面
                                                 'city_id': city_id,  # 返回从url里面读取到的city信息
                                                 'sort': sort,  # 返回从url里面读取到的排序信息
                                                 'hot_orgs': hot_orgs,  # 返回根据点击数得到的排序信息
                                                 'count': count})


class Comments_Upload(View):
    """
    这个是测试用的，主要是测试ajax的动态上传数据方法
    """
    def post(self, request):
        print('It\'s a Test')  # 用于测试
        print(request.POST['name'])  # 测试是否能够接收到前端发来的name字段
        print(request.POST['password'])  # 用户同上面

        return HttpResponse('表单测试成功!')  # 最后返会给前端的数据，如果能在前端弹出框中显示我们就成功了
        #return render(request, 'test_ajax_1.html', {'msg': '表单测试成功!'})

    def get(self, request):
        return render(request, 'test_ajax_1.html', {})


class CustomAddView(View):
    def get(self, request):
        a = request.GET.get('a', '')
        b = request.GET.get('b', '')
        print('我被GET方法调用')
        return render(request, 'test_ajax_2.html', {})

    def post(self, request):
        a = request.POST.get('a', '')
        b = request.POST.get('b', '')
        print('我被POST方法调用')
        return render(request, 'test_ajax_2.html', {})


class CustomAjaxView(View):
    """
    收到AjaxView，处理AjaxView
    """
    def get(self, request):
        print(u'我们好')
        return render(request, 'AJaxTest_3.html', {})

    def post(self, request):
        ret = {'status': 1001,
               'error': ''}
        user = request.POST.get('username', '')
        pwd = request.POST.get('userpassword','')
        print(user, pwd)
        if user == 'freeman' and pwd == '123456':
            ret['status'] = 1002
        else:
            ret['error'] = 'Username or password Error!'
        return HttpResponse(json.dumps(ret))
