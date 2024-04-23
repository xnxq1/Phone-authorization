import string
import random
from django.core.cache import cache
from django.conf import settings
from celery import shared_task
from django.http import HttpResponse
from twilio.rest import Client
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


@shared_task()
def _get_pin(length=5):
    return random.sample(range(10 ** (length - 1), 10 ** length), 1)[0]


@shared_task()
def _verify_pin(mobile_number, pin):
    return pin == cache.get(mobile_number)


@shared_task()
def send_pin(mobile_number):
    """ Sends SMS PIN to the specified number """
    pin = _get_pin()
    print(pin)
    # store the PIN in the cache for later verification.
    cache.set(mobile_number, pin, 24 * 3600)  # valid for 24 hrs

    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="%s" % pin,
        to=mobile_number,
        from_=settings.TWILIO_FROM_NUMBER,
    )
