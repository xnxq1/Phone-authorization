
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Номер телефона', widget=forms.TextInput(attrs={'placeholder': '+79999999999'}))
    password = forms.CharField(max_length=100, label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'пароль'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if username[0] != '+' and any(username[i].isalpha() for i in range(1, len(username))):
            raise forms.ValidationError('Номер телефона написан неправильно')

        return username