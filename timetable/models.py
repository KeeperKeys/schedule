from datetime import time

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db import models

# from django.core.signals import
# from django.dispatch import receiver
# from django.core.signals import

from coursework import settings


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Email непрменно должен быть указан')
        user = self.model(
            email=UserManager.normalize_email(email)
        )
        user.set_password(password)
        user.user_type = 3
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.user_type = 0
        user.is_superuser = True
        user.save(using=self._db)
        return user


class ExtUser(AbstractBaseUser, PermissionsMixin):
    TYPE_ADMIN = 0  # is superuser
    TYPE_TEACHER = 1  # is staff
    TYPE_ELDER = 2
    TYPE_STUDENT = 3
    TYPE_CHOICES = (
        (TYPE_ADMIN, 'Администратор'),
        (TYPE_TEACHER, 'Преподователь'),
        (TYPE_ELDER, 'Староста'),
        (TYPE_STUDENT, 'Студент')
    )

    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=255,
        unique=True,
        db_index=True
    )
    avatar = models.ImageField(
        verbose_name='Аватар',
        blank=True,
        null=True,
        upload_to="user/avatar"
    )
    first_name = models.CharField(
        verbose_name='Фамилия',
        max_length=40,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        verbose_name="Имя",
        max_length=40,
        blank=True,
        null=True
    )
    middle_name = models.CharField(
        verbose_name="Отчество",
        max_length=40,
        blank=True,
        null=True
    )
    date_of_birth = models.DateField(
        verbose_name="Дата рождения",
        blank=True,
        null=True
    )
    user_type = models.IntegerField(
        verbose_name="Тип пользователя",
        choices=TYPE_CHOICES,
    )
    register_date = models.DateField(
        verbose_name="Дата регистрации",
        auto_now_add=True,
    )
    is_active = models.BooleanField(
        verbose_name="Активен",
        default=True
    )
    # is_admin = models.BooleanField(
    # "Статус персонала",
    # help_text='Отметьте, если пользователь может входить в административную часть сайта.',
    # default=False
    # )

    def get_full_name(self):
        # Возможно, следует изменить на "{0} {1} {2}".format(self.first_name, self.last_name, self.middle_name)
        return self.email

    @property
    def is_staff(self):
        return self.user_type == 0 or self.user_type == 1

    def get_short_name(self):
        return self.email

    # def is_stud

    def __str__(self):
        # Разобраться какой метод что и когда возвращает
        # return self.email
        return "{0} {1} {2}".format(self.first_name, self.last_name, self.middle_name)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = UserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ('first_name', 'last_name', 'middle_name')


class Faculty(models.Model):
    title = models.CharField(
        verbose_name="Название факультета",
        max_length=255,
        help_text="Польное название факультета",
        unique=True,
    )
    abbreviation_uk = models.CharField(
        verbose_name="Аббревиатура на украинском",
        max_length=10,
        help_text="Сокращенная запись название факультета на украинском",
        unique=True
    )
    abbreviation_en = models.CharField(
        verbose_name="Аббревиатура на английском",
        max_length=10,
        help_text="Сокращенная запись название факультета на английском",
        unique=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Факультет"
        verbose_name_plural = "Факультеты"
        ordering = ('title',)


class Discipline(models.Model):
    # если придумаю ещё какие-то поля, то добавлю
    title = models.CharField(
        verbose_name="Название дисциплины",
        max_length=255,
        help_text="Полное название учебной дисциплины",
        unique=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"
        ordering = ('title',)


class Housing(models.Model):
    title = models.CharField(
        verbose_name="Название корпуса",
        help_text="Полное название",
        max_length=255,
        unique=True
    )
    abbreviation_uk = models.CharField(
        verbose_name="Аббревиатура на украинском",
        help_text="Сокращенная запись название корпуса на украинском",
        max_length=127,
        unique=True
    )
    abbreviation_en = models.CharField(
        verbose_name="Аббревиатура на английском",
        help_text="Сокращенная запись название корпуса на английском",
        max_length=127,
        unique=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Корпус"
        verbose_name_plural = "Корпуса"
        ordering = ('title',)


class UniversityGroup(models.Model):
    faculty = models.ForeignKey(
        to='Faculty',
        verbose_name="Факультет",
        help_text="Полное название факультета"
    )
    number_uk = models.CharField(
        verbose_name="Номер группы на украинском",
        help_text="Указывать прописные буквы",
        max_length=30,
        # null=True,
    )
    number_en = models.CharField(
        verbose_name="Номер группы на английском",
        help_text="Указывать прописные буквы",
        max_length=30,
        # null=True,
    )
    title_uk = models.CharField(
        verbose_name="Полное название группы на украинском",
        max_length=255,
        editable=False,
        # null=True,
    )
    title_en = models.CharField(
        verbose_name="Полное название группы на английском",
        max_length=255,
        editable=False,
        # null=True,
    )

    def return_title(self):
        return self.faculty.abbreviation_uk.__str__() + '-' + self.number_uk.__str__()

    def __str__(self):
        return self.title_uk

    def save(self, *args, **kwargs):
        self.number_uk = self.number_uk.__str__().upper()
        self.title_uk = self.return_title()

        self.number_en = self.number_en.__str__().upper()
        self.title_en = self.faculty.abbreviation_en.__str__() + '-' + self.number_en.__str__()
        super(UniversityGroup, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Учебная группа"
        verbose_name_plural = "Учебные группы"
        ordering = ('title_uk',)


class WeekDay(models.Model):
    title = models.CharField(
        verbose_name="День недели",
        max_length=20
    )

    short_title = models.CharField(
        verbose_name="Сокращенное название",
        max_length=5
    )

    number = models.SmallIntegerField(
        verbose_name="Номер дня недели по порядку",
        # editable=False
    )


    # def save(self, *args, **kwargs):
    #     if self.title=="Понедельник"
    #     self.number = self.return_title()
    #     super(WeekDay, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "День недели"
        verbose_name_plural = "Дни недели"
        ordering = ('number',)


class LessonTime(models.Model):
    starting = models.TimeField(
        verbose_name="Время начала"
    )
    ending = models.TimeField(
        verbose_name="Время окончания"
    )
    number = models.SmallIntegerField(
        verbose_name="Номер занятия",
        help_text="По порядку, в течении дня"
    )

    def __str__(self):
        return self.starting.__str__()

    class Meta:
        verbose_name = "Время занятия"
        verbose_name_plural = "Время занятий"
        ordering = ('starting',)


class Lesson(models.Model):
    WEEK_TOP = 'top'
    WEEK_BOTTOM = 'bottom'
    WEEK_BOTH = 'both'
    CHOICE_WEEK = (
        (WEEK_TOP, "Верхняя"),
        (WEEK_BOTTOM, "Нижняя"),
        (WEEK_BOTH, 'Обе недели'),
    )
    title_discipline = models.ForeignKey(
        to="Discipline",
        verbose_name="Название дисциплины",
        help_text="Полное название учебной дисциплины",
    )
    teacher = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name="Преподаватель",
        help_text="Преподаватель проводящий данное занятие",
        null=True,
        blank=True
    )
    week = models.CharField(
        verbose_name="Неделя",
        choices=CHOICE_WEEK,
        max_length=10,
        default=WEEK_BOTH
    )
    weekday = models.ForeignKey(
        to='WeekDay',
        verbose_name="День недели",
    )
    time = models.ForeignKey(
        to='LessonTime',
        verbose_name="Время проведения занятия",
    )
    housing = models.ForeignKey(
        to='Housing',
        verbose_name="Корпус",
        help_text="Полное назваие корпуса",
        null=True,
        blank=True,
    )
    audience = models.CharField(
        verbose_name="Аудитория",
        max_length=5,
        null=True,
        blank=True
    )
    update_date = models.DateTimeField(
        auto_now=True
    )
    group = models.ForeignKey(
        to='UniversityGroup',
        verbose_name="Учебная группа",
        help_text="Полное название учебной группы"
    )

    title = models.CharField(
        verbose_name="Время проведения",
        max_length=255,
        editable=False,
    )

    def return_title(self):
        return self.group.title_uk.__str__() + ": " + self.weekday.short_title.__str__() + " " + self.time.starting.__str__()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.return_title()
        super(Lesson, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Занятие"
        verbose_name_plural = "Занятия"
        ordering = ('title',)


class Comment(models.Model):
    subject = models.CharField(
        verbose_name="Тема комментария",
        max_length=127,
    )
    comment = models.TextField(
        verbose_name="Комментарий"
    )
    file = models.FileField(
        verbose_name="Прикрепленный файл",
        upload_to='teacher/comment/file',
        blank=True,
        null=True,
        # help_text="Только архивы: *.rar, *.zip, *.7z"
    )
    date_time = models.DateTimeField(
        verbose_name="Дата и врем комментария",
        auto_now=True
    )
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Отправитель",
        null=True,
        blank=True,
        editable=False
    )
    lesson = models.ForeignKey(
        to='Lesson',
        verbose_name="Занятие",
        help_text="К какому занятию прикрепить данный комментарий"
    )
    title = models.CharField(
        verbose_name="Название комментария для сортировок",
        max_length=255,
        editable=False,
    )

    def return_title(self):
        return self.sender.__str__() + ": " + self.subject.__str__()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.return_title()
        super(Comment, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ('title',)
