from django.core.exceptions import ValidationError
from django import forms
def validate_username(username):
    if username[0] != '+' and any(username[i].isalpha() for i in range(1, len(username))):
        raise forms.ValidationError('Номер телефона написан неправильно')

