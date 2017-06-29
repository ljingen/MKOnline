# -*- encoding:utf-8 -*-
import time

from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic import View
from .models import UserProfile, EmailVerifyCode
from .forms import LoginForm, RegisterForm, ForgetPwdForm, ModifyPwdForm
from utils.email_send import my_send_mail

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
            filter_user_result = UserProfile.objects.filter(username=username)
            if len(filter_user_result) > 0:
                errors.append('用户名已经存在!')
                return render(request, 'register.html', {'register_form': register_form, 'errors': errors})
            # 保存用户的信息
            user = UserProfile()
            user.username = username
            # 因为django是加密保存密码，所以需要使用django.contrib.auth.hashers import make_password
            user.password = make_password(password1)
            user.email = username
            user.is_active = False
            user.save()
            # 保存成功后，给用户发送一封激活认证邮件
            send_status = my_send_mail(username, 'register')
            # 登录前需要先验证,并直接返回到已经登录的用户首页
            new_user = authenticate(username=username, password=password1)
            if new_user is not None:
                login(request, new_user)
                return render(request, 'index.html', {})
            else:
                return render(request, 'register.html', {'register_form': register_form})
        except Exception as e:
            return render(request, 'register.html', {'register_form': register_form})


class ActiveUserView(View):
    """
    get: 激活用户，根据url捕获的code，查到对应的email，再根据email，查找到对应的user，
    然后将user.is_active的状态设置为True
    """
    def get(self, request, active_code):
        # print(type(active_code))
        email_verify = EmailVerifyCode.objects.get(code=active_code, send_type='register')
        if email_verify:
            email = email_verify.email
            my_user = UserProfile.objects.get(email=email)
            if my_user:
                my_user.is_active = True
                my_user.save()
                return render(request, 'active_user_success.html', {})
            else:
                return render(request, 'login.html', {'msg':u'用户不存在或没找到!'})
        return render(request, 'login.html', {'msg':u'验证码失效或验证码错误,请重试!'})


class ForgetPwdView(View):
    """
    作用:用户点击找回密码，进入到这个视图进行处理， url(r'^forget_pwd/$', ForgetPwdView.as_view(), name='')
    get(self, request) : 初始化一个验证码，根据验证码，返回一个填写邮箱找回密码的页面
    post(self,request)
    """
    def get(self, request):
        forget_pwd_form = ForgetPwdForm()
        return render(request, 'forgetpwd.html', {'forget_pwd_form': forget_pwd_form})

    def post(self, request):
        forget_pwd_form = ForgetPwdForm(request.POST)
        if forget_pwd_form.is_valid():
            email = request.POST['email']
            # 根据输入的邮箱地址，查找该邮箱地址是否有对应的账户
            user = UserProfile.objects.filter(email=email)
            if user:
                send_status = my_send_mail(email, 'forget')
                if send_status:
                    return render(request, 'send_forgetpwd_success.html.html', {})
                else:
                    return render(request, 'forgetpwd.html', {'forget_pwd_form': forget_pwd_form,
                                                              'email': email,
                                                              'msg': '邮件发送失败,请重试!'})
            else:
                return render(request, 'forgetpwd.html', {'forget_pwd_form': forget_pwd_form,
                                                          'email': email,
                                                          'msg': u'用户不存在!'})
        else:
            return render(request, 'forgetpwd.html', {'forget_pwd_form': forget_pwd_form})


class ResetPwdView(View):
    """
    get: 重置密码入口，根据url捕获的code，查到对应的email，返回给用户进入到密码修改页面，在该页面，将email带入进去。
    然后修改密码时，根据邮箱、密码，进行修改用户的密码
    """
    def get(self, request, reset_code):
        # print(type(active_code))
        email_verify = EmailVerifyCode.objects.get(code=reset_code, send_type='forget')
        if email_verify:
            email = email_verify.email
            my_user = UserProfile.objects.get(email=email)
            if my_user:
                return render(request, 'password_reset.html', {'email':email})
            else:
                return render(request, 'forgetpwd.html', {'msg':u'用户不存在或没找到!'})
        return render(request, 'forgetpwd.html', {'msg':u'验证码失效或验证码错误,请重试!'})


class ModifyPwdView(View):
    """
    post: 用户在修改密码的页面，输入新密码，老密码，点击提交,提交post请求的时候，进入到这个视图
    """
    def post(self, request):
            modify_pwd_form = ModifyPwdForm(request.POST)
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            email = request.POST['email']
            user = UserProfile.objects.get(email=email)
            if modify_pwd_form.is_valid():
                if password1 == password2:
                    if user:
                        user.password = make_password(password1)
                        return render(request, 'login.html', {})
                    else:
                        return render(request, 'password_reset.html', {'email':email, 'msg': u'用户不存在'})
                else:
                    return render(request, 'password_reset.html', {'modify_pwd_form':modify_pwd_form, 'email': email})
            else:
                return render(request, 'password_reset.html', {'modify_pwd_form': modify_pwd_form, 'email': email})
