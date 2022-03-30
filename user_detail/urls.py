from rest_framework import routers
from django.urls import path
from user_detail import views
from user_detail import view_detail
from .views import *

router= routers.DefaultRouter()

urlpatterns = [
    path ('user_detail/user_list/', views.detail_list, name='detail_list'),
    path ('user_detail/UsersDetails/<int:pk>/', views.UsersDetails, name='UsersDetails'),
    path ('user_detail/', view_detail.UserDetailList.as_view(queryset=user_detail.objects.all(), serializer_class=UserDetailSerializer))
    
]

urlpatterns += router.urls