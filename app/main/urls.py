from django.contrib import admin
from django.urls import path, include
from . import views
from . import tasks
app_name = 'main'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('register/', views.Register.as_view(), name='register'),
    path('verify/', views.Verify.as_view(), name='verify'),
]
