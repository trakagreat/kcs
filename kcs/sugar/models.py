from django.db import models

# Create your models here.
class ClientModel(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
