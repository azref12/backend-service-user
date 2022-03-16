from rest_framework import serializers
from .models import user_follow

class FollowSerializer(serializers.ModelSerializer):
        class Meta:
                model = user_follow
                fields = ['id','follow'] 