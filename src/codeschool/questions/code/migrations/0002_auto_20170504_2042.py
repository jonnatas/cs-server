# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-04 20:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('code', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CodeQuestionFeedback',
            new_name='CodeFeedback',
        ),
        migrations.RenameModel(
            old_name='CodeQuestionProgress',
            new_name='CodeProgress',
        ),
        migrations.RenameModel(
            old_name='CodeQuestionSubmission',
            new_name='CodeSubmission',
        ),
    ]