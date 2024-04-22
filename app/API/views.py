from django.contrib.auth.models import User
from django.contrib.messages import api
from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import apiSerializer
from main.models import ReferralProgram
# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response


class apiViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    def retrieve(self, request, pk=None):
        referral = ReferralProgram.objects.get(user_owner__id=pk)

        serializer = apiSerializer(referral)
        return Response(serializer.data)