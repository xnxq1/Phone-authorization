# Generated by Django 4.2.11 on 2024-04-22 02:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='referralprogram',
            name='referral_users',
            field=models.ManyToManyField(related_name='referral', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Referral',
        ),
    ]
