import string
import random

from celery import shared_task
from .models import ReferralProgram


@shared_task()
def create_referral_token(user):
    referral_token = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    ReferralProgram.objects.create(user_owner=user, token=referral_token)

    return referral_token


@shared_task()
def add_referral_user(referral_token, user):
    if not referral_token:
        return
    referral_obj = ReferralProgram.objects.select_for_update().filter(token=referral_token).first()
    referral_obj.referral_users.add(user)
    return referral_obj.token
