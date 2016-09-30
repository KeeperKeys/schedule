# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0006_auto_20151125_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekday',
            name='number',
            field=models.SmallIntegerField(verbose_name='Номер дня недели по порядку'),
        ),
    ]
