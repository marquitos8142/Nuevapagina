from django.db import models

# Create your models here.


class Programmer(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=3)
    birthday = models.DateField()
    score = models.DecimalField(max_digits=10, decimal_places=5)

    class Meta:
        db_table = 'programmer' 
