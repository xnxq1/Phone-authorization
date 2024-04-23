import random

from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import LoginForm, RegisterForm, VerifyForm
from .tasks import create_referral_token,add_referral_user, send_pin
from django.contrib import messages
from django.shortcuts import redirect

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
            with transaction.atomic():
                user = form.save(commit=False)
                request['user'] = user
                #user.set_password(form.cleaned_data['password1'])
                #user.save()
                request['user_referral_token'] = create_referral_token(user)
                request['authorization_referral_token'] = add_referral_user(self.request.POST.get('referral_token'), user)

            return redirect(to='main:verify')

        return HttpResponse('Что-то пошло не так')



class Verify(View):

    def get(self, request):
        phone = request.GET.get('user')
        send_pin(phone)
        return render(request, 'verify.html', {'form': VerifyForm()})




