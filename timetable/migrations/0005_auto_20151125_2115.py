# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0004_auto_20151125_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='time',
            field=models.ForeignKey(verbose_name='Время проведения занятия', to='timetable.LessonTime'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='weekday',
            field=models.ForeignKey(verbose_name='День недели', to='timetable.WeekDay'),
        ),
    ]
