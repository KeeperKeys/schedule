from django import forms


class DantzigForm(forms.Form):
    dimension = forms.IntegerField(min_value=1, max_value=15)
