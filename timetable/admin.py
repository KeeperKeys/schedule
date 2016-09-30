from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from timetable.forms import UserChangeForm, UserCreationForm, LessonForm
from timetable.models import ExtUser, Faculty, Discipline, Comment, Lesson, Housing, UniversityGroup, LessonTime, \
    WeekDay


class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = [
        'first_name',
        'last_name',
        'middle_name',
        'user_type',
        'email',
    ]

    list_filter = ('user_type',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {
            'fields': (
                'avatar',
                'first_name',
                'last_name',
                'middle_name',
                'date_of_birth'
            )
        }),
        ('Permissions', {'fields': ('is_active', 'user_type')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields' : (
                'email',
                'password1',
                'password2',
                'user_type',
                'date_of_birth'
            )
        }),
    )

    search_fields = ('email',)
    ordering = ('first_name', 'last_name', 'middle_name',)
    filter_horizontal = ()


class FacultyAdmin(admin.ModelAdmin):
    list_display = ('title', 'abbreviation_uk', 'abbreviation_en',)
    search_fields = ('title', 'abbreviation_uk', 'abbreviation_en',)
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields' : ('title', 'abbreviation_uk', 'abbreviation_en',),
        }),
    )
    ordering = ('title',)


class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields' : ('title',),
        }),
    )
    ordering = ('title',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('sender', 'lesson', 'subject', 'date_time')
    search_fields = ('sender__email', 'subject', 'lesson')
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields' : ('subject', 'comment', 'lesson'),
        }),
        ("Прикрепленный файл", {
            'classes': ('wide',),
            'fields' : ('file',),
        }),
    )
    ordering = ('sender', 'lesson')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'sender', None) is None:
            obj.sender = request.user
        obj.save()


class HousingAdmin(admin.ModelAdmin):
    list_display = ('title', 'abbreviation_uk', 'abbreviation_en',)
    search_fields = ('title', 'abbreviation_uk', 'abbreviation_en',)
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields' : ('title', 'abbreviation_uk', 'abbreviation_en',),
        }),
    )
    ordering = ('title',)


class UniversityGroupAdmin(admin.ModelAdmin):
    list_display = ('faculty', 'title_uk', 'title_en')
    search_fields = ('faculty__title', 'title_uk', 'title_en')
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields' : ('faculty', 'number_uk', 'number_en',),
        }),
    )
    ordering = ('faculty', 'title_uk',)


class LessonAdmin(admin.ModelAdmin):
    form = LessonForm

    list_display = ('title', 'week', 'title_discipline', 'teacher', 'housing', 'audience',)
    search_fields = ('title',)
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields' : ('group', 'teacher', 'title_discipline', 'housing', 'audience', 'weekday', 'week', 'time'),
        }),
    )

    ordering = ('title', '-week')
    radio_fields = {'week': admin.VERTICAL}
    list_filter = ('group__title_uk',)


class LessonTimeAdmin(admin.ModelAdmin):
    list_display = ('starting', 'ending', 'number',)
    fields = ('starting', 'ending', 'number',)
    ordering = ('starting',)


class WeekDayAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_title',)  # , 'max_title')
    fields = ('title', 'short_title', 'number',)
    ordering = ('number',)


admin.site.register(ExtUser, UserAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Housing, HousingAdmin)
admin.site.register(UniversityGroup, UniversityGroupAdmin)
admin.site.register(LessonTime, LessonTimeAdmin)
admin.site.register(WeekDay, WeekDayAdmin)
admin.site.unregister(Group)
