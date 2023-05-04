from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet

from .models import UserFunction
from .serializers import UserSerializer
# Create your views here.

class UserView(ModelViewSet):
    queryset=  UserFunction.objects.all()
    serializer_class= UserSerializer