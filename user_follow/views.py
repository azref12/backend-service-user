from inspect import isfunction
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
import datetime
from .serializers import FollowSerializer
from .models import user_follow
from rest_framework.response import Response

t = datetime.datetime.now()
mastermodel = isfunction
masterserialzer = isfunction

if __name__ == "__main__":
    print(user_follow.objects.all())

@csrf_exempt
@api_view(["GET","POST"])
@permission_classes([IsAuthenticated]) 
def follow_list (request) :
    
    try:
        cek = request.GET['return_url']
        if  cek == '/follow_list':
            mastermodel = user_follow
            masterserialzer = FollowSerializer
            
    except cek.DoesNotExist:
        return HttpResponse(status=500)
    
    if request.method == 'GET':
        
        mastermodel = user_follow
        masterserialzer = FollowSerializer
        
        localmodel = mastermodel.objects.all()
        localserializer = masterserialzer(localmodel, many=True)
        
        return Response({'message' : 'successfully', 'status' : True, 'count' : 1, 
                             'results' : localserializer.data})
        
    elif request.method == 'POST':
            
            masterserialzer = FollowSerializer
            
            localrequest = JSONParser().parse(request)
            localserializer = masterserialzer(data=localrequest)
            print(localrequest) 
            
            if localserializer.is_valid():
                if  cek == '/follow_list' :
                    
                    follows = user_follow (
                                            id = localserializer.data.get("id"),
                                            follow = localserializer.data.get("follow")
                                        )
                    follows.save()
                    localmodel = mastermodel.objects.all()
                    localserializer = masterserialzer(localmodel, many=True)
                                    
                    return JsonResponse({'message' : 'successfully', 'status' : True, 'count' : 1, 
                                     'results' : localserializer.data}, status=201)
                return JsonResponse(localserializer.errors, status=400)

@csrf_exempt
@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated])  
def follow_detail (request, pk) :
        try:
                cek = request.GET['return_url']
                if  cek == '/follow_detail':
                        mastermodel = user_follow
                        masterserialzer = FollowSerializer
                
        except cek.DoesNotExist:
                return HttpResponse(status=500)
        
        try:    
                mastermodel = user_follow

                localmodel = mastermodel.objects.get(pk=pk)
        except mastermodel.DoesNotExist:
                return HttpResponse(status=404)

        if request.method == 'GET':
                masterserialzer = FollowSerializer
                
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
 