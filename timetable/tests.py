# from django.test import TestCase
# from timetable.models import UniversityGroup, WeekDay, LessonTime, Lesson
#
# class TimetableTestCase(TestCase):
# def setUp(self):

from datetime import datetime

from timetable.models import UniversityGroup, Lesson, WeekDay, LessonTime, ExtUser, Comment


group = UniversityGroup.objects.get(title_en="IF-34B")
day_of_week = WeekDay.objects.get(pk=2)
time = LessonTime.objects.get(number=3)
week_type = 'top'
res_lesson = Lesson.objects.filter(group=group).filter(weekday=day_of_week).filter(time=time).get(week=week_type)

user = ExtUser.object.get(pk=3)

new_comment = Comment(subject="Тестовый комментарий", comment="Содержание текстового коментария",
                      date_time=datetime.now(), sender=user,
                      lesson=res_lesson)