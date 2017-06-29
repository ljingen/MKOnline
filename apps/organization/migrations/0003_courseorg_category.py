# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-28 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20170626_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='category',
            field=models.CharField(choices=[('pxjg', '培训机构'), ('gx', '高校'), ('gr', '个人')], default='pxjg', max_length=5, verbose_name='类别'),
        ),
    ]
