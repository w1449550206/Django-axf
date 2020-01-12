from django.db import models

# Create your models here.

class AxfFoodType(models.Model):
    typeid = models.CharField(max_length=32)
    typename = models.CharField(max_length=64)
    childtypenames = models.CharField(max_length=256)
    typesort = models.IntegerField()

    class Meta:
        db_table='axf_foodtype'

