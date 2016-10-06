from django.db import models

# Create your models here.
class registrado(models.Model):
    codigo = models.IntegerField(blank=True,null=True)
    nombre = models.CharField(max_length=60,blank=False ,null=False)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)#saber el momento en el que se registro
    actualizado = models.DateTimeField(auto_now_add=False,auto_now=True)#saber el momento en el que se hizo un cambio

def __str__(self):
    return self.codigo
