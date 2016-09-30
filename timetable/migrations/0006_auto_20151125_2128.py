# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0005_auto_20151125_2115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weekday',
            options={'verbose_name': 'День недели', 'ordering': ('number',), 'verbose_name_plural': 'Дни недели'},
        ),
        migrations.AddField(
            model_name='weekday',
            name='number',
            field=models.SmallIntegerField(verbose_name='Номер дня недели по порядку', null=True),
        ),
    ]
