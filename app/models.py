from django.db import models

# Create your models here.


class Programmer(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'programmer' 
