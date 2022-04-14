from rest_framework import serializers
from django.contrib.auth.models import User
from account.models import user_detail
from .models import *
# from account.serializers import RegistrationSerializer
               
class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True}
        }

class UserSerializer(serializers.ModelSerializer):
        # id_users = RegistrationSerializer (read_only=True, many=True)
        
        class Meta:
                model = user_detail
                fields = "__all__"
