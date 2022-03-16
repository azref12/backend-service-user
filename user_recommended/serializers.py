from rest_framework import serializers
from .models import user_recommended

class UserRecommendedSerializer(serializers.ModelSerializer):
        class Meta:
                model = user_recommended
                fields = ['id','user_recommended']