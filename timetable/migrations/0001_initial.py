# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('email', models.EmailField(verbose_name='Электронная почта', max_length=255, unique=True, db_index=True)),
                ('avatar', models.ImageField(verbose_name='Аватар', upload_to='user/avatar', null=True, blank=True)),
                ('first_name', models.CharField(verbose_name='Фамилия', max_length=40, null=True, blank=True)),
                ('last_name', models.CharField(verbose_name='Имя', max_length=40, null=True, blank=True)),
                ('middle_name', models.CharField(verbose_name='Отчество', max_length=40, null=True, blank=True)),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения', null=True, blank=True)),
                ('user_type', models.IntegerField(verbose_name='Тип пользователя', choices=[(0, 'Администратор'), (1, 'Преподователь'), (2, 'Староста'), (3, 'Студент')])),
                ('register_date', models.DateField(verbose_name='Дата регистрации', auto_now_add=True)),
                ('is_active', models.BooleanField(verbose_name='Активен', default=True)),
                ('groups', models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', blank=True, related_query_name='user', verbose_name='groups', to='auth.Group', related_name='user_set')),
                ('user_permissions', models.ManyToManyField(help_text='Specific permissions for this user.', blank=True, related_query_name='user', verbose_name='user permissions', to='auth.Permission', related_name='user_set')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'ordering': ('first_name', 'last_name', 'middle_name'),
                'verbose_name_plural': 'Пользователи',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('subject', models.CharField(verbose_name='Тема комментария', max_length=127)),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('file', models.FileField(verbose_name='Прикрепленный файл', upload_to='teacher/comment/file', null=True, blank=True)),
                ('date_time', models.DateTimeField(verbose_name='Дата и врем комментария', auto_now=True)),
                ('title', models.CharField(verbose_name='Название комментария для сортировок', max_length=255, editable=False)),
            ],
            options={
                'verbose_name': 'Комментарий преподователя',
                'ordering': ('title',),
                'verbose_name_plural': 'Комментарии преподователей',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Название дисциплины', max_length=255, help_text='Полное название учебной дисциплины')),
            ],
            options={
                'verbose_name': 'Дисциплина',
                'ordering': ('title',),
                'verbose_name_plural': 'Дисциплины',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Название факультета', max_length=255, help_text='Польное название факультета')),
                ('abbreviation_uk', models.CharField(verbose_name='Аббревиатура на украинском', max_length=10, help_text='Сокращенная запись название факультета на украинском')),
                ('abbreviation_en', models.CharField(verbose_name='Аббревиатура на английском', max_length=10, help_text='Сокращенная запись название факультета на английском')),
            ],
            options={
                'verbose_name': 'Факультет',
                'ordering': ('title',),
                'verbose_name_plural': 'Факультеты',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Housing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Название корпуса', max_length=255, help_text='Полное название')),
                ('abbreviation_uk', models.CharField(verbose_name='Аббревиатура на украинском', max_length=127, help_text='Сокращенная запись название корпуса на украинском')),
                ('abbreviation_en', models.CharField(verbose_name='Аббревиатура на английском', max_length=127, help_text='Сокращенная запись название корпуса на английском')),
            ],
            options={
                'verbose_name': 'Корпус',
                'ordering': ('title',),
                'verbose_name_plural': 'Корпуса',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('weekday', models.SmallIntegerField(verbose_name='День недели', choices=[(1, 'Понедельник'), (2, 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятница')])),
                ('time_start', models.TimeField(verbose_name='Время начала', choices=[(datetime.time(8, 30), '08:30:00'), (datetime.time(10, 25), '10:25:00'), (datetime.time(12, 35), '12:35:00'), (datetime.time(14, 30), '14:30:00'), (datetime.time(16, 25), '16:25:00'), (datetime.time(18, 10), '18:10:00')])),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(verbose_name='Название занятия для сортировок', max_length=255, editable=False)),
            ],
            options={
                'verbose_name': 'Занятие',
                'ordering': ('title',),
                'verbose_name_plural': 'Занятия',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UniversityGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.CharField(verbose_name='Номер группы', max_length=30, help_text='Указывать строчные буквы')),
                ('title', models.CharField(verbose_name='Название факультета для сортировок', max_length=255, editable=False)),
                ('faculty', models.ForeignKey(help_text='Полное название факультета', verbose_name='Факультет', to='timetable.Faculty')),
            ],
            options={
                'verbose_name': ('Учебная группа',),
                'ordering': ('title',),
                'verbose_name_plural': ('Учебные группы',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='lesson',
            name='group',
            field=models.ForeignKey(help_text='Полное название учебной группы', verbose_name='Учебная группа', to='timetable.UniversityGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lesson',
            name='housing',
            field=models.ForeignKey(help_text='Полное назваие корпуса', verbose_name='Корпус', to='timetable.Housing'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(help_text='Преподователь проводящий данное занятие', null=True, blank=True, verbose_name='Преподаватель', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lesson',
            name='title_discipline',
            field=models.ForeignKey(help_text='Полное название учебной дисциплины', verbose_name='Название дисциплины', to='timetable.Discipline'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='lesson',
            field=models.ForeignKey(help_text='К какому занятию прикрепить данный комментарий', verbose_name='Занятие', to='timetable.Lesson'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='sender',
            field=models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL, editable=False),
            preserve_default=True,
        ),
    ]
