# -*- encoding:utf-8 -*-
import time

from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic import View
from .models import UserProfile
from .forms import LoginForm, RegisterForm

# Create your views here.


class CustomBackend(ModelBackend):
    """
    用户认证后台
    自定义的用户认证后台，支持邮箱或者手机号或者username进行系统登录
    """
    def authenticate(self, username=None, password=None, **kwargs):
        # Check the username/password and return a User.
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username) | Q(phone=username))
            if user.check_password(password):
                return user
            else:
                return None
        except Exception as e:
            return None


class LoginView(View):
    """
    用户登录类
    用户get页面，则返回用户的当前登录页面
    用户post请求，根据请求结果
    登录成功，则返回到首页
    登录失败，则返回当前登录页，并将错误信息返回到前端展示给用户，错误的输入框高亮显示
    """
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # Redirect to a success page.
                    return render(request, 'index.html', {'login_form': login_form})
                else:
                    return render(request, 'login.html', {'msg': '用户还没有被激活', 'login_form': login_form})
            else:
                # Return an 'invalid login' error message
                return render(request, 'login.html', {'msg': '用户名或密码错误,请重试!'})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class RegisterView(View):
    """
    用户注册类
    get:返回当前的注册页面，提供注册验证码
    用户post请求，根据请求结果
    登录成功，则返回到首页
    登录失败，则返回当前登录页，并将错误信息返回到前端展示给用户，错误的输入框高亮显示
    """
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        curtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        register_form = RegisterForm(request.POST)

        if request.user.is_authenticated():
            return HttpResponseRedirect('/index')
        try:
            username = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            errors = []

            if not register_form.is_valid():
                return render(request, 'register.html', {'register_form': register_form})
            if password1 != password2:
                errors.append('两次密码不一致!')
                return render(request, 'register.html', {'register_form': register_form, 'errors': errors})
            filter_user_result = UserProfile.objects.filter(username = username)
            if len(filter_user_result)>0:
                errors.append('用户名已经存在!')
                return render(request, 'register.html', {'register_form': register_form, 'errors': errors})
            # 保存用户的信息
            user = UserProfile()
            user.username = username
            user.password = make_password(password1)
            user.email = username
            user.is_active = True
            user.save()
            # 登录前需要先验证,并直接返回到已经登录的用户首页
            new_user = authenticate(username=username, password=password1)
            if new_user is not None:
                login(request, new_user)
                return render(request, 'index.html', {})
            else:
                return render(request, 'register.html', {'register_form': register_form})
        except Exception as e:
            return render(request, 'register.html', {'register_form': register_form})


