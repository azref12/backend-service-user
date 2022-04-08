from rest_framework import serializers
from django.contrib.auth.models import User
from .models import user_detail

class UserSerializer(serializers.ModelSerializer):
        class Meta:
                model = user_detail
                fields = "__all__"
                
class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True}
        }