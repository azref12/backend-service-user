from rest_framework import routers
from django.urls import path
from user_recommended import views
from user_recommended import view_recommended
from .views import *

router= routers.DefaultRouter()

urlpatterns = [
    path ('user_recommended/recommended_lists/', views.recommended_list, name='recommended_list'),
    path ('user_recommended/recommended_details/<int:pk>/', views.recommended_detail, name='recommended_detail'),
    path ('user_recommended/', view_recommended.RecommendedList.as_view(queryset = user_recommended.objects.all(),
                                                       serializer_class = UserRecommendedSerializer))
]

urlpatterns += router.urls 