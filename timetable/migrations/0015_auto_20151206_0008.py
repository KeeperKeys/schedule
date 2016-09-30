# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0014_auto_20151205_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universitygroup',
            name='title_uk',
            field=models.CharField(verbose_name='Полное название группы на украинском', max_length=255, editable=False),
        ),
    ]
