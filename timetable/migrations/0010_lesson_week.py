# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0009_auto_20151130_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='week',
            field=models.CharField(null=True, verbose_name='Неделя', help_text='Верхняя/нижняя', choices=[('top', 'Верхняя'), ('bottom', 'Нижняя')], max_length=10),
        ),
    ]
