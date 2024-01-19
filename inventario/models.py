from typing import Any
from django.db import models

# Create your models here.
class Productos(models.Model):
    
    nombre = models.CharField(max_length=30) #este campo, va a ser creado solamente como CARACTERES
    precio = models.FloatField()
    stock = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.nombre
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'producto'
        verbose_name_plural = 'Productos'
        
