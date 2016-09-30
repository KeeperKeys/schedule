# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0013_auto_20151205_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universitygroup',
            name='number_en',
            field=models.CharField(help_text='Указывать строчные буквы', verbose_name='Номер группы на английском', max_length=30),
        ),
        migrations.AlterField(
            model_name='universitygroup',
            name='number_uk',
            field=models.CharField(help_text='Указывать строчные буквы', verbose_name='Номер группы на украинском', max_length=30),
        ),
        migrations.AlterField(
            model_name='universitygroup',
            name='title_en',
            field=models.CharField(verbose_name='Полное название группы на английском', max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='universitygroup',
            name='title_uk',
            field=models.CharField(verbose_name='Полное название группы на русском', max_length=255, editable=False),
        ),
    ]
