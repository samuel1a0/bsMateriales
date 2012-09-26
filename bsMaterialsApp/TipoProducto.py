from django.db import models

class TipoProducto(models.Model):
    nombre = models.CharField(max_length=50)
    #unidadMedida= models.CharField()
    descripcion= models.CharField(max_length=100)
    #rubro  
    
    def __unicode__(self):
        return u"%s" % self.nombre