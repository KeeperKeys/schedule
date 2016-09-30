# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0012_auto_20151205_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='universitygroup',
            name='number',
        ),
        migrations.AddField(
            model_name='universitygroup',
            name='number_en',
            field=models.CharField(null=True, help_text='Указывать строчные буквы', verbose_name='Номер группы на английском', max_length=30),
        ),
        migrations.AddField(
            model_name='universitygroup',
            name='number_uk',
            field=models.CharField(null=True, help_text='Указывать строчные буквы', verbose_name='Номер группы на украинском', max_length=30),
        ),
    ]
