from django.db import models
from django.contrib.auth.models import User


class user_detail (models.Model):
    id_role = models.AutoField(primary_key=True)
    role = models.IntegerField(blank=False, null=True, default=4)
    id_users = models.ForeignKey(
        User, related_name='id_users_id', on_delete=models.CASCADE)
    reward = models.IntegerField(blank=False,default=0)
    point = models.IntegerField(blank=False,default=0)
    coin = models.IntegerField(blank=False,default=0)
    phone_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    app_id = models.IntegerField(blank=False,default=0)

    def __str__(self):
        return self.role
