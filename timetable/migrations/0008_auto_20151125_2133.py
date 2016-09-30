# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0007_auto_20151125_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessontime',
            name='ending',
            field=models.TimeField(verbose_name='Время окончания'),
        ),
    ]
