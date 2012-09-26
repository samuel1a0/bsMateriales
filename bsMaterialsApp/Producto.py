from django.db import models
from TipoProducto import TipoProducto

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    stockT= models.IntegerField()
    tipoProducto = models.ForeignKey(TipoProducto)
    descripcion= models.CharField(max_length=100)
    
    def __unicode__(self):
        return u"%s" % self.nombre