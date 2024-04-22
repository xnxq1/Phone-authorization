import string
import random

from celery import shared_task
from .models import ReferralProgram

@shared_task()
def create_referral_token(user):
    referral_token = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    ReferralProgram.objects.create(user_owner=user, token=referral_token)

    return referral_token
