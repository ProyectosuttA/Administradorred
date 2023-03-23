from django.db import models

class Datos(models.Model):
    host=models.CharField(max_length=20)
    user=models.CharField(max_length=20)
    tipo=models.CharField(max_length=20)
    password=models.CharField(max_length=30)
    pactivo=models.BooleanField(default=True)


# Create your models here.
