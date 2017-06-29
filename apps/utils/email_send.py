# -*- encoding:utf-8 -*-
from random import Random

from django.core.mail import send_mail
from users.models import EmailVerifyCode
from MXonline.settings import EMAIL_FROM

__author__ = 'Amos'
__date__ = '2017/6/22 11:58'


# 生成验证码的随机code
def generate_random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890'
    length = len(chars)-1
    random = Random()
    # 生成在0 到 长度之间的随机整数；
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def my_send_mail(email, send_type='register'):
    # 1、先生成一个验证码并保存到数据库，供后续激活使用
    email_recode = EmailVerifyCode()
    email_recode.email = email
    email_recode.send_type = send_type
    code = generate_random_str(16)
    email_recode.code = code
    email_recode.save()

    # 2 组合一个注册邮件的激活信息
    if send_type == 'register':
        email_title = '慕学网在线注册激活链接'
        email_body = '请点击下面的链接激活您的账号:http://127.0.0.1:8000/active/{0}'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            return send_status
        else:
            return None
    if send_type == 'forget':
        email_title = '慕学网重置密码'
        email_body = '请点击下面的链接重置你的密码:http://127.0.0.1:8000/reset/{0}'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            return send_status
        else:
            return None