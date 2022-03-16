from django.db import models

class user_like (models.Model) :
    id = models.AutoField(primary_key=True) 
    user_like = models.IntegerField(blank=False,default=0)
    
    def __str__(self) :
        return self.user_like 
