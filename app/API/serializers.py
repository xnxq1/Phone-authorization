from rest_framework import serializers
from main.models import ReferralProgram
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class apiSerializer(serializers.ModelSerializer):
    referral_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = ReferralProgram
        fields = ('user_owner', 'token', 'referral_users', )
