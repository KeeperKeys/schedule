# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'Комментарии', 'verbose_name': 'Комментарий', 'ordering': ('title',)},
        ),
        migrations.AlterModelOptions(
            name='universitygroup',
            options={'verbose_name_plural': 'Учебные группы', 'verbose_name': 'Учебная группа', 'ordering': ('title',)},
        ),
        migrations.AlterField(
            model_name='discipline',
            name='title',
            field=models.CharField(unique=True, help_text='Полное название учебной дисциплины', verbose_name='Название дисциплины', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='faculty',
            name='abbreviation_en',
            field=models.CharField(unique=True, help_text='Сокращенная запись название факультета на английском', verbose_name='Аббревиатура на английском', max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='faculty',
            name='abbreviation_uk',
            field=models.CharField(unique=True, help_text='Сокращенная запись название факультета на украинском', verbose_name='Аббревиатура на украинском', max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='faculty',
            name='title',
            field=models.CharField(unique=True, help_text='Польное название факультета', verbose_name='Название факультета', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='housing',
            name='abbreviation_en',
            field=models.CharField(unique=True, help_text='Сокращенная запись название корпуса на английском', verbose_name='Аббревиатура на английском', max_length=127),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='housing',
            name='abbreviation_uk',
            field=models.CharField(unique=True, help_text='Сокращенная запись название корпуса на украинском', verbose_name='Аббревиатура на украинском', max_length=127),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='housing',
            name='title',
            field=models.CharField(unique=True, help_text='Полное название', verbose_name='Название корпуса', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(verbose_name='Преподаватель', help_text='Преподователь проводящий данное занятие', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
