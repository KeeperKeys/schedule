# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0010_lesson_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='week',
            field=models.CharField(help_text='Верхняя/нижняя', verbose_name='Неделя', choices=[('top', 'Верхняя'), ('bottom', 'Нижняя')], max_length=10),
        ),
    ]
