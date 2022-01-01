from django.db import models
from django.db.models.fields import CharField,IntegerField
# Create your models here.

class Employe(models.Model):
    name = models.CharField(max_length = 15)
    age = models.IntegerField()
    position = models.CharField(max_length= 15)

    def __str__(self):
        return self.name
