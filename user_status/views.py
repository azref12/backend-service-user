from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import FilterSet
from django_filters import rest_framework as filters
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from inspect import isfunction
from msilib.schema import AppId
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
import datetime
from pathlib import Path
from decouple import Config ,RepositoryEnv, Csv
import os
from rest_framework import generics
from .serializers import UserStatusSerializer
from .models import user_status

t = datetime.datetime.now()

if __name__ == "__main__":
    print(user_status.objects.all())
    
class UserStatusList (generics.ListCreateAPIView) :
        queryset = user_status.objects.all()
        serializer_class = UserStatusSerializer
        DecodedGenerator = api_view
        permission_classes = [AllowAny]
        filter_backends = [SearchFilter, OrderingFilter]
        search_fields = ['id','user_status'] 

class UserStatusDetail (generics.RetrieveUpdateDestroyAPIView) :
        queryset = user_status.objects.all()
        serializer_class = UserStatusSerializer
        DecodedGenerator = api_view
        permission_classes = [AllowAny]
        filter_backends = [SearchFilter, OrderingFilter]
        search_fields = ['id','user_status']