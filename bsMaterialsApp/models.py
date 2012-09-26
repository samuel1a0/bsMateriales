from django.db import models
# Create your models here.

#=====================================
# Modelos de producto
#=====================================
class TipoProducto(models.Model):
    nombre = models.CharField(max_length=50)
    #unidadMedida= models.CharField()
    descripcion= models.CharField(max_length=100)
    #rubro  
    def __unicode__(self):
        return u"%s" % self.nombre.strip()

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    stockT= models.IntegerField()
    #tipoProducto = models.ForeignKey(TipoProducto)
    descripcion= models.CharField(max_length=100)
    
    def __unicode__(self):
        return u"%s" % self.nombre
    
