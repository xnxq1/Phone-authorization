from django.forms import forms
from django.shortcuts import render
from django.contrib.auth.views import LoginView
# Create your views here.

class Login(LoginView):
    template_name = 'login.html'
