# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0008_auto_20151125_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='audience',
            field=models.CharField(max_length=5, null=True, verbose_name='Аудитория', blank=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='housing',
            field=models.ForeignKey(null=True, blank=True, to='timetable.Housing', verbose_name='Корпус', help_text='Полное назваие корпуса'),
        ),
    ]
