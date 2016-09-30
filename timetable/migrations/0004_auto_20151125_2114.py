# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0003_auto_20151125_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('starting', models.TimeField(verbose_name='Время начала')),
                ('ending', models.DateTimeField(verbose_name='Время окончания')),
                ('number', models.SmallIntegerField(verbose_name='Номер занятия', help_text='По порядку, в течении дня')),
            ],
            options={
                'ordering': ('starting',),
                'verbose_name': 'Время занятия',
                'verbose_name_plural': 'Время занятий',
            },
        ),
        migrations.CreateModel(
            name='WeekDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(verbose_name='День недели', max_length=20)),
                ('short_title', models.CharField(verbose_name='Сокращенное название', max_length=5)),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'День недели',
                'verbose_name_plural': 'Дни недели',
            },
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='time_start',
        ),
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(editable=False, verbose_name='Время проведения', max_length=255),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='weekday',
            field=models.ForeignKey(to='timetable.WeekDay', null=True, verbose_name='День недели'),
        ),
        migrations.AlterField(
            model_name='universitygroup',
            name='title',
            field=models.CharField(editable=False, verbose_name='Полное название группы', max_length=255),
        ),
        migrations.AddField(
            model_name='lesson',
            name='time',
            field=models.ForeignKey(to='timetable.LessonTime', null=True, verbose_name='Время проведения занятия'),
        ),
    ]
