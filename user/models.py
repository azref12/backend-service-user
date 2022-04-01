from django.db import models

class Users (models.Model) :
    id = models.AutoField(primary_key=True) 
    first_name = models.CharField(max_length = 100, null = False)
    last_name = models.CharField(max_length = 100, null = False)
    username = models.CharField(max_length = 50, null = False) 
    email = models.CharField(max_length = 200, null = False)
    reward = models.IntegerField(blank=False,default=0)
    point = models.IntegerField(blank=False,default=0)
    coin = models.IntegerField(blank=False,default=0)
    active = models.SmallIntegerField(blank=False,default=0)
    phone_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    app_id = models.IntegerField(blank=False,default=0)
    
    def __str__(self) :
        return self.username, self.first_name, self.last_name
