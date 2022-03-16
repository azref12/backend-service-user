from django.db import models

class group (models.Model) :
    id = models.AutoField(primary_key=True) 
    group_name = models.CharField(max_length=100, null=False)
    
    def __str__(self) :
        return self.group_name
