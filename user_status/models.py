from django.db import models

class user_status (models.Model) :
    id = models.AutoField(primary_key=True) 
    user_status = models.CharField(max_length=100, null=False)
    
    def __str__(self) :
        return self.user_status
