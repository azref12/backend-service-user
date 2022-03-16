from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
        class Meta:
                model = User
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