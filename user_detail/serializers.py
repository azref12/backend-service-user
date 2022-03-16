from rest_framework import serializers
from .models import user_detail

class UserDetailSerializer(serializers.ModelSerializer):
        class Meta:
                model = user_detail
                fields = ['id','profile_user','profile_bussines']