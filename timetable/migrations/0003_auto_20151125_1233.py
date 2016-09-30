# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_auto_20151101_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='sender',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Отправитель', editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='extuser',
            name='groups',
            field=models.ManyToManyField(blank=True, to='auth.Group', related_name='user_set', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user'),
        ),
        migrations.AlterField(
            model_name='extuser',
            name='last_login',
            field=models.DateTimeField(verbose_name='last login', blank=True, null=True),
        ),
    ]
