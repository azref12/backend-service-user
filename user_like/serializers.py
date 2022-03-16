from rest_framework import serializers
from .models import user_like
class UserLikeSerializer(serializers.ModelSerializer):
        class Meta:
                model = user_like
                fields = ['id','user_like']