from rest_framework import serializers
from .models import group

class GroupSerializer(serializers.ModelSerializer):
        class Meta:
                model = group
                fields = ['id','group_name']