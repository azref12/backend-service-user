from email.generator import DecodedGenerator
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
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
from .serializers import UserSerializer
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
import datetime
from pathlib import Path
from decouple import Config ,RepositoryEnv, Csv
import os
from rest_framework import generics
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

t = datetime.datetime.now()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOTENV_FILE = './config/.env'
getenv = Config(RepositoryEnv(DOTENV_FILE))
APP_ID=getenv('APP_ID')

if __name__ == "__main__":
    print(User.objects.all())
    

class UserList (generics.ListCreateAPIView) :
        queryset = User.objects.all()
        serializer_class = UserSerializer
        DecodedGenerator = api_view
        permission_classes = [AllowAny]
        filter_backends = [SearchFilter, OrderingFilter]
        filterset_fields = ['id', 'username','email'] 
        ordering_fields = ['id','username', 'email']
        search_fields = ['id','username', 'email']

class UsersDetail (generics.RetrieveUpdateDestroyAPIView) :
        queryset = User.objects.all()
        serializer_class = UserSerializer
        DecodedGenerator = api_view
        permission_classes = [AllowAny]
        filter_backends = [SearchFilter, OrderingFilter]
        filterset_fields = ['id', 'username','email'] 
        ordering_fields = ['id','username', 'email']
        search_fields = ['id','username', 'email']

        
        

        
        

        


                
            
            
        

        
        
                
                