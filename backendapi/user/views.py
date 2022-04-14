#from rest_framework.response import Response
#from rest_framework.authtoken.views import ObtainAuthToken
#from django.shortcuts import render
#from rest_framework.renderers import JSONRenderer
#from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from inspect import isfunction
from msilib.schema import AppId
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import RegistrationSerializer, UserSerializer
from django.contrib.auth.models import User
from account.models import user_detail
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
import datetime
from pathlib import Path
from decouple import Config ,RepositoryEnv, Csv
import os
from re import X
from django.db import DatabaseError, transaction
from django.db.utils import IntegrityError

t = datetime.datetime.now()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOTENV_FILE = './config/.env'
getenv = Config(RepositoryEnv(DOTENV_FILE))
APP_ID=getenv('APP_ID')

if __name__ == "__main__":
    print(user_detail.objects.all())

mastermodel = isfunction
masterserialzer = isfunction

@csrf_exempt
@api_view(["GET","POST"])
@permission_classes([AllowAny])

def User_list (request):    
        try:
                cek = request.GET['return_url']
                if  cek == '/users':
                        mastermodel = User
                        masterserialzer = RegistrationSerializer
                        
                        mymodels = user_detail
                        serializerss = UserSerializer
                
        except cek.DoesNotExist:
                return HttpResponse(status=500)

        if request.method == 'GET':
                localmodel = mastermodel.objects.all()
                localserializer = masterserialzer(localmodel, many=True)
                
                localmodels = mymodels.objects.all()
                localserializers = serializerss (localmodels, many=True)
                
                formater = {
                        "master" : localserializer.data,
                        "detail" : localserializers.data
                }
                return JsonResponse({'message' : 'successfully' , 'status' : True , 'count' : 1 , 'results' : formater},
                                status=201)

        if request.method == 'POST':
                localrequest = JSONParser().parse(request)
                localserializer = masterserialzer(data=localrequest)
                if localserializer.is_valid():
                        try:
                                res = User.objects.filter(id).last()
                                x = int (res.id)+1
                                print(x)
                        except :
                                x=1
                                
                        with transaction.atomic():
                                sid = transaction.savepoint()
                                try:
                                        usersave = User (
                                                id = localrequest.get['id'],
                                                password = localrequest.get['password'],
                                                last_login = localrequest.get['last_login'],
                                                is_superuser = localrequest.get['is_superuser'],
                                                username = localrequest.get['username'], 
                                                first_name = localrequest.get['first_name'], 
                                                last_name = localrequest.get['last_name'],
                                                email = localrequest.get['email'],
                                                is_staff = localrequest.get['is_staff'],
                                                is_active = localrequest.get['is_active'],
                                                date_joined = localrequest.get['date_joined']
                                        )
                                        usersave.save()
                                        
                                        for obj in localrequest :
                                                id_userss = user_detail.objects.filter(id_users = obj['id_users']).first()
                                                
                                                details = user_detail (
                                                        id_users = id_userss,
                                                        id_role = obj.get['id_role'],
                                                        role = obj.get['role'],
                                                        reward = obj.get['reward'],
                                                        point = obj.get['point'],
                                                        coin = obj.get['coin'],
                                                        phone_number = obj.get['phone_number'],
                                                        app_id = APP_ID
                                                )
                                                details.save()
                                        transaction.savepoint_commit(sid)
                                except IntegrityError:
                                        transaction.savepoint_rollback(sid)

                                mastermodel = User.objects.all()
                                masterserialzer = RegistrationSerializer (mastermodel, many=True)
                                        
                                mymodels = user_detail.objects.all() 
                                serializerss = UserSerializer (mymodels, many=True)
                                        
                                formater = {
                                        "master" : masterserialzer.data,
                                        "detail" : serializerss.data
                                }
                                
                                return JsonResponse({'message' : 'successfully' , 'status' : True , 'count' : 1 , 'results' : formater},
                                        status=201)  

@csrf_exempt
@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([AllowAny])  
def Users_details(request, pk):
        try:
                cek = request.GET['return_url']
                if  cek == '/users':
                        mastermodel = User
                        masterserialzer = RegistrationSerializer
                
        except cek.DoesNotExist:
                return HttpResponse(status=500)
        
        try:
                localmodel = mastermodel.objects.get(pk=pk)
        except mastermodel.DoesNotExist:
                return HttpResponse(status=404)

        if request.method == 'GET':
        
                localserializer = masterserialzer(localmodel)
                return JsonResponse(localserializer.data)
    
        elif request.method == 'PUT': 
                localrequest = JSONParser().parse(request) 
                localserializer = masterserialzer(localmodel, data=localrequest) 

                if localserializer.is_valid(): 
                
                        localserializer.save()  
                
                        localmodel = mastermodel.objects.all()
                        localserializer = masterserialzer(localmodel, many=True)

                        return JsonResponse({'message' : 'successfully' , 'status' : True , 'count' : 1 , 'results' : localserializer.data},
                                        status=201)
                return JsonResponse(localserializer.errors, status=400) 

        elif request.method == 'PATCH':
                localserializer = masterserialzer(localmodel, data={'status':0}, partial=True)
                if localserializer.is_valid():
                        localserializer.save()
                        return JsonResponse({'message': 'Success'}, status=200)
                else:
                        return JsonResponse(localserializer.errors, status=400)

        elif request.method == 'DELETE': 
                localmodel.delete() 
                localmodel = mastermodel.objects.all()
                localserializer = masterserialzer(localmodel, many=True)

        return JsonResponse({'message' : 'successfully' , 'status' : True , 'count' : 1 , 'results' : localserializer.data},
                                status=201)        

