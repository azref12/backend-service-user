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
from .serializers import UserSerializer
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
    print(User.objects.all())

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
                        masterserialzer = UserSerializer
                
        except cek.DoesNotExist:
                return HttpResponse(status=500)

        if request.method == 'GET':
                localmodel = mastermodel.objects.all()
                localserializer = masterserialzer(localmodel, many=True)
                return JsonResponse({'message' : 'successfully' , 'status' : True , 'count' : 1 , 'results' : localserializer.data},
                                status=201)

        if request.method == 'POST':
                mastermodel = User
                masterserialzer = UserSerializer
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

                                        if localserializer.is_valid():
                                                users = User.objects.filter(id = localrequest['id']).first()

                                                UserSave = User ( 
                                                                id = users,
                                                                first_name=localserializer.data.get("first_name"),
                                                                last_name=localserializer.data.get("last_name"),
                                                                username=localserializer.data.get("username"),
                                                                email=localserializer.data.get("email"),
                                                                reward=localserializer.data.get("reward"),
                                                                point=localserializer.data.get("point"),
                                                                coin=localserializer.data.get("coin"),
                                                                active = localserializer.data.get("active"),
                                                                phone_number = localserializer.data.get("phone_number"),
                                                                app_id = APP_ID,
                                                        )
                                                UserSave.save()
                                        transaction.savepoint_commit(sid)
                                except IntegrityError:
                                        transaction.savepoint_rollback(sid)

                                ModelMaster = User.objects.filter(id)
                                MasterSerializer = UserSerializer(ModelMaster, many=True)
                                
                                formater = {
                                        "master": MasterSerializer.data

                                }
                            
                                return JsonResponse({'message' : 'successfully' , 'status' : True , 'count' : 1 , 'results' : formater},
                                    status=201)  

@csrf_exempt
@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([AllowAny])  
def Users_details(request, pk):
        try:
                cek = request.GET['return_url']
                if  cek == '/user_details':
                        mastermodel = User
                        masterserialzer = UserSerializer
                
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
