from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render

from django.views import View
from django.views.generic import TemplateView

from .forms import LoginForm, RegisterForm


# Create your views here.
def check_auth(request):
    if request.user.is_authenticated:
        return True
    return False


class Login(View):

    def get(self, request):
        if check_auth(request):
            return HttpResponse("Вы авторизованы")
        return render(request, 'login.html', {'form': LoginForm()})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('Вы авторизовались')
            return HttpResponse('Такого пользователя не существует')

        return HttpResponse('Что-то пошло не так')


class Logout(View):
    def get(self, request):
        if not check_auth(request):
            return HttpResponse('Вы не авторизованы')
        logout(request)
        return HttpResponse('Вы вышли из аккаунта')

class Register(View):

    def get(self, request):
        if check_auth(request):
            return HttpResponse('Вы авторизованы')

        return render(request, 'register.html', {'form': RegisterForm()})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():

            user = form.save(commit=False)

            user.set_password(form.cleaned_data['password1'])
            user.save()

            login(request, user)

            return HttpResponse('Вы зарегистрировались')

        return HttpResponse('Что-то пошло не так')
