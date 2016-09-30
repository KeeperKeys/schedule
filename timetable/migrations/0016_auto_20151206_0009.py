# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0015_auto_20151206_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(null=True, help_text='Преподователь проводящий данное занятие', verbose_name='Преподаватель', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
