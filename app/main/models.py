from django.contrib.auth.models import User
from django.db import models


class ReferralProgram(models.Model):
    token = models.CharField(max_length=255, unique=True, default=0, verbose_name="Токен")
    user_owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    referral_users = models.ManyToManyField(User, related_name='referral', blank=True)

    class Meta:
        ordering = ['user_owner']
        verbose_name = 'Реферальная программа - Токен'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.user_owner}: {self.token}'



