from django.shortcuts import render_to_response, RequestContext
from timetable.models import UniversityGroup, Lesson, WeekDay, LessonTime, Comment
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.http import Http404
from django.db.models import Q
import sqlite3
# from dicttoxml import dicttoxml
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
import traceback
# import pdfkit


def main_page(request):
    return render_to_response('main.html', context_instance=RequestContext(request))


def groups(request):
    qs = UniversityGroup.objects.all()
    return render_to_response('groups.html', {'groups': qs}, context_instance=RequestContext(request))


def selected_group(request, group_title, html_path='selected_group.html'):
    res_dict = {}
    # получение группы по названию, ошибка игнорируется
    group = UniversityGroup.objects.get(title_en=group_title.upper())
    res_dict['group'] = group
    # получение занятий этой группы
    lessons_all = Lesson.objects.filter(group__title_en__exact=group_title.upper())
    res_dict['lessons_all'] = lessons_all

    schedule = list()

    # получение всех дней ндели
    days = WeekDay.objects.all()
    working_days = 5
    res_dict['days'] = days[:working_days]  # первые 5 дней недели

    # формирование расписания сложной вложенной структуры, добавление его в словарь и возвращение представления
    for day in days[:working_days]:
        time_lessons_all = list()
        for time in LessonTime.objects.all():
            lessons = tuple(Lesson.objects.filter(group__title_en=group_title.upper()).filter(weekday=day).filter(
                time=time))
            time_lessons = (time, lessons,)
            time_lessons_all.append(time_lessons)
        schedule.append((day, time_lessons_all,))
    res_dict['schedule'] = schedule
    # render = render_to_response(html_path, res_dict, context_instance=RequestContext(request))
    # render = render.getvalue().decode('utf-8')
    return render_to_response(html_path, res_dict, context_instance=RequestContext(request))


def teachers_xml(request):
    conn = sqlite3.connect('db.sqlite3')
    curs = conn.cursor()
    res = curs.execute(
        'SELECT first_name, last_name, middle_name FROM timetable_extuser WHERE user_type==1 OR user_type==1')
    all_teacher = res.fetchall()
    xml = ""
    # xml = dicttoxml(all_teacher, custom_root='teachers')
    response = HttpResponse(content_type='application/xml')
    response['Content-Disposition'] = 'filename="teachers.xml"'
    response.write(xml)
    return response


def selected_group_pdf(request, group_title):
    render = selected_group(request, group_title, html_path='selected_group_pdf.html')
    render = render.getvalue().decode('utf-8')
    # написать крутой код через потоки, который будет в отображении делать представление, отдвать его
    # а затем в левом потоке сохранять этот файл. пока создавать хардкорно каждый раз файлы
    # file = mmap.mmap(-1, 10000)
    file_path = 'timetable/groups/pdf/group_{0}.pdf'.format(group_title)
    file = open(file_path, 'w')
    file.close()
    # pdfkit.from_string(render, file_path)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="{0}"'.format(file_path)
    file = open(file_path, 'rb')
    res_pdf = file.read(-1)
    response.write(res_pdf)
    file.close()
    return response


def selected_lesson(request, group_title, day_of_week, time, week_type):
    res_dict = {}
    # попытка получить по group_title объект группы
    try:
        group_title = UniversityGroup.objects.get(title_en=group_title.upper())
    except ObjectDoesNotExist:
        group_title = None
        traceback.print_exc()

    # попытка превратить day_of_week в число и получить по этому числу объект дня недели
    try:
        day_of_week = int(day_of_week)
        day_of_week = WeekDay.objects.get(pk=day_of_week)
    except (ValueError, ObjectDoesNotExist):
        day_of_week = None
        traceback.print_exc()

    # попытка превратить time в число и получить по этому числу объект времени урока
    try:
        time = int(time)
        time = LessonTime.objects.get(number=time)
    except (ValueError, ObjectDoesNotExist):
        time = None
        traceback.print_exc()

    if week_type not in ('top', 'bottom', 'both'):
        week_type = None

    if group_title and day_of_week and time and week_type:
        try:
            res_lesson = Lesson.objects.filter(group=group_title).filter(weekday=day_of_week).filter(time=time).get(
                week=week_type)
            res_dict['lesson'] = res_lesson
        except ObjectDoesNotExist:
            traceback.print_exc()
            raise Http404("Не корректные данные")
        except MultipleObjectsReturned:
            traceback.print_exc()
            raise Http404
    else:
        raise Http404("Не корректные данные")

    if request.user.is_authenticated() and request.method == 'POST':
        subject = request.POST['subject']
        comment = request.POST['comment']
        new_comment = Comment(subject=subject, comment=comment, date_time=datetime.now(), sender=request.user,
                              lesson=res_lesson)
        # if subject and comment:
        new_comment.save()
        return HttpResponseRedirect('')

    teachers_comments = Comment.objects.filter(lesson=res_lesson).filter(
        Q(sender__user_type=1) | Q(sender__user_type=0)).order_by('date_time')
    res_dict['teacher_comments'] = teachers_comments
    students_comments = Comment.objects.filter(lesson=res_lesson).filter(
        Q(sender__user_type=2) | Q(sender__user_type=3)).order_by('date_time')
    res_dict['students_comments'] = students_comments
    # sorted(teachers_comments,reverse=True)
    # sorted(students_comments)
    if request.user.is_authenticated() and request.user.is_staff:
        res_dict['is_staff'] = True
    if request.user.is_authenticated() and not request.user.is_staff:
        res_dict['not_staff'] = True
    res_dict['null_res'] = "уточнить на кафедре"
    return render_to_response('selected_lesson.html', res_dict, context_instance=RequestContext(request))
