# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-26 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='image',
            field=models.ImageField(default='image/default.png', upload_to='org/%Y/%m', verbose_name='封面图'),
        ),
    ]