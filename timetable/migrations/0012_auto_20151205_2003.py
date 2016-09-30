# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0011_auto_20151130_1749'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='universitygroup',
            options={'ordering': ('title_uk',), 'verbose_name': 'Учебная группа', 'verbose_name_plural': 'Учебные группы'},
        ),
        migrations.RemoveField(
            model_name='universitygroup',
            name='title',
        ),
        migrations.AddField(
            model_name='universitygroup',
            name='title_en',
            field=models.CharField(null=True, editable=False, verbose_name='Полное название группы на английском', max_length=255),
        ),
        migrations.AddField(
            model_name='universitygroup',
            name='title_uk',
            field=models.CharField(null=True, editable=False, verbose_name='Полное название группы на русском', max_length=255),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='week',
            field=models.CharField(choices=[('top', 'Верхняя'), ('bottom', 'Нижняя'), ('both', 'Обе недели')], default='both', verbose_name='Неделя', max_length=10),
        ),
    ]
