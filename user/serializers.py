from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
        class Meta:
                model = Users
                fields = [
                        'id',
                        'first_name',
                        'last_name',
                        'username',
                        'email',
                        'reward',
                        'point',
                        'coin',
                        'active',
                        'phone_number',
                        'created_at',
                        'last_login']