from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from timetable.models import Lesson, ExtUser


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Подтверждение",
        widget=forms.PasswordInput
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Пароль и подтверждение не совпадают')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('email',)


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        widget=forms.PasswordInput,
        required=False
    )

    def clean_password(self):
        return self.initial['password']


def save(self, commit=True):
    user = super(UserChangeForm, self).save(commit=False)
    password = self.cleaned_data['password']
    if password:
        user.set_password(password)
    if commit:
        user.save()
    return user


class Meta:
    model = get_user_model()
    fields = ['email', ]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class LessonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LessonForm, self).__init__(*args, **kwargs)
        self.fields['teacher'].queryset = ExtUser.object.filter(user_type__exact='1')

    class Meta:
        model = Lesson
        fields = '__all__'
        # exclude = ['teacher']

# class LessonForm(forms.Form):
