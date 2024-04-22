from django.contrib.auth import authenticate, login
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views import View
from django.views.generic import TemplateView

from .forms import LoginForm


# Create your views here.

class Login(View):

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponse('Вы авторизованы')

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
