#from django.shortcuts import render
from inspect import isfunction
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer
# from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
import datetime
from .serializers import UserDetailSerializer
from .models import user_detail
# from re import X
# from django.db.utils import IntegrityError
# from django.db import transaction
from rest_framework.response import Response
from rest_framework import status

t = datetime.datetime.now()
mastermodel = isfunction
masterserialzer = isfunction

if __name__ == "__main__":
    print(user_detail.objects.all())

@csrf_exempt
@api_view(["GET","POST"])
@permission_classes([IsAuthenticated]) 
def user_listing (request) :
    
    try:
        cek = request.GET['return_url']
        if  cek == '/users_listings':
            mastermodel = user_detail
            masterserialzer = UserDetailSerializer
            
    except cek.DoesNotExist:
        return HttpResponse(status=500)
    
    if request.method == 'GET':
        
        mastermodel = user_detail
        masterserialzer = UserDetailSerializer
        
        localmodel = mastermodel.objects.all() 
        localserializer = masterserialzer(localmodel, many=True)
        
        return JsonResponse({'message' : 'successfully' , 'status' : True , 'count' : 1 , 
                             'results' : localserializer.data})
        
    elif request.method == 'POST':
            
            masterserialzer = UserDetailSerializer
            
            localrequest = JSONParser().parse(request)
            localserializer = masterserialzer(data=localrequest)
            print(localrequest)
            
            if localserializer.is_valid():
                if  cek == '/users_listings' :
                    
                    detail_user = user_detail(
                                                profile_user = localserializer.data.get("profile_user"),
                                                profile_bussines= localserializer.data.get("profile_bussines"),
                                            )
                    detail_user.save()
                    localmodel = mastermodel.objects.all()
                    localserializer = masterserialzer(localmodel, many=True)
                                    
                    return JsonResponse({'message' : 'successfully', 'status' : True, 'count' : 1, 
                                         'results' : localserializer.data}, status=201)
                return JsonResponse(localserializer.errors, status=400) 
    
@csrf_exempt
@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated]) 
def UserDetails (request, pk) :
        try:
                cek = request.GET['return_url']
                if  cek == '/UserDetails':
                        mastermodel = user_detail
                        masterserialzer = UserDetailSerializer
                
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

    
                
                