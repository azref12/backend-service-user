from tokenize import group
from rest_framework import routers
from django.urls import path
from group import views
from group import view_group
from .views import *

router= routers.DefaultRouter()

urlpatterns = [
    path ('group/groups/', views.group_list, name='group_List'),
    path ('group/group_detail/<int:pk>/', views.group_detail, name='group_detail'),
    path ('group/', view_group.GroupList.as_view(queryset=group.objects.all(), serializer_class=GroupSerializer))
]

urlpatterns += router.urls  