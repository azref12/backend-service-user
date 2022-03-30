from rest_framework import routers
from django.urls import path, include
from user import views
from user import view_generic
from .views import *
from .customejwt import LogoutView, MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    #TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    # TokenObtainSlidingView,
    # TokenRefreshSlidingView,
)

router= routers.DefaultRouter()

urlpatterns = [
    path ('', include (router.urls)),
    path ('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path ('token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
    path ('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path ('logout/', LogoutView.as_view(), name='auth_logout'),
    path ('user/users/', views.User_list, name='User_List'),
    path ('user/user_details/<int:pk>/', views.Users_details, name='Users_details'),
    path ('user/', view_generic.UserList.as_view(queryset=User.objects.all(), serializer_class=UserSerializer), name='UserList')
]


urlpatterns += router.urls
