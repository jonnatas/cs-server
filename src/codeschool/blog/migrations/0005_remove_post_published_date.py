# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-12 00:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_comment_approved_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
    ]