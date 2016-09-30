# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0016_auto_20151206_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(verbose_name='Преподаватель', blank=True, to=settings.AUTH_USER_MODEL, help_text='Преподаватель проводящий данное занятие', null=True),
        ),
        migrations.AlterField(
            model_name='universitygroup',
            name='number_en',
            field=models.CharField(max_length=30, help_text='Указывать прописные буквы', verbose_name='Номер группы на английском'),
        ),
        migrations.AlterField(
            model_name='universitygroup',
            name='number_uk',
            field=models.CharField(max_length=30, help_text='Указывать прописные буквы', verbose_name='Номер группы на украинском'),
        ),
    ]
