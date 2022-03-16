from rest_framework import serializers
from .models import user_status

class UserStatusSerializer(serializers.ModelSerializer):
        class Meta:
                model = user_status
                fields = ['id','user_status']