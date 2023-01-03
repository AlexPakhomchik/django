from django.db import models


class Materials(models.Model):
    type_of_material = models.CharField(max_length=200)
    amount = models.IntegerField()
# Create your models here.
