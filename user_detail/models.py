from django.db import models

class user_detail (models.Model) :
    id = models.AutoField(primary_key=True) 
    profile_user = models.CharField(max_length=100, null=False)
    profile_bussines = models.CharField(max_length=100, null=False)
    
    def __str__(self) :
        return self.profile_user, self.profile_bussines 
