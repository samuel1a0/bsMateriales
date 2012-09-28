from django.db import models
# Create your models here.

class Rubro(models.Model):
    nombre = models.CharField(max_length = 40)
    descripcion = models.CharField(max_length = 40, blank=True)
    
    def __unicode__(self):
        return "%s" % self.nombre
#---------------------------------------------------------------------------------------------------

class TipoProducto(models.Model):
    nombre = models.CharField(max_length = 40)
    unidad_de_medida = models.CharField(max_length = 40)
    descripcion = models.CharField(max_length = 40, blank=True)
    rubro = models.ForeignKey(Rubro)
    
    def __unicode__(self):
        return "%s" % self.nombre
#---------------------------------------------------------------------------------------------------

class Producto(models.Model):
    nombre = models.CharField(max_length = 40)
    stock_total = models.IntegerField()
    tipo_de_producto = models.ForeignKey(TipoProducto)
    descripcion = models.CharField(max_length = 40, blank = True)
    
    def __unicode__(self):
        return "%s" % self.nombre
#---------------------------------------------------------------------------------------------------

class Producto_Fraccionable(Producto):
    medida = models.CharField(max_length = 40)
#---------------------------------------------------------------------------------------------------

class Producto_No_Fraccionable(Producto):
    pass
#---------------------------------------------------------------------------------------------------

class Deposito(models.Model):
    rubro = models.ForeignKey(Rubro)
    direccion = models.CharField(max_length = 40)
    telefono = models.CharField(max_length = 15)
    
    def __unicode__(self):
        return "%s" % self.rubro
#---------------------------------------------------------------------------------------------------

class Detalle(models.Model):
    cantidad = models.IntegerField()
    sub_total = models.IntegerField()
    producto = models.ForeignKey(Producto)
#----------------------------------------------------------------------------------------------------

class Detalle_Nota_Venta(Detalle):
    pass
#----------------------------------------------------------------------------------------------------

class Detalle_Factura(Detalle):
    venta = models.ForeignKey(Detalle_Nota_Venta)
    pass
#----------------------------------------------------------------------------------------------------

class Nota_Venta(models.Model):
    nro_nota = models.IntegerField()
    nombre_cliente = models.CharField(max_length = 40)
    apellido_cliente = models.CharField(max_length = 20)
    fecha = models.datetime    
    detalle = models.ForeignKey(Detalle_Nota_Venta)
#----------------------------------------------------------------------------------------------------

class Factura(models.Model):
    nro_factura = models.IntegerField()
    fecha = models.datetime
    formaDePago = models.CharField(max_length = 15)
    precio_total = models.IntegerField()
    venta_nota = models.ForeignKey(Nota_Venta)
    detalle = models.ForeignKey(Detalle_Factura)    
#----------------------------------------------------------------------------------------------------

class Detalle_Remito(models.Model):
    producto = models.ForeignKey(Producto)
    cantidad = models.IntegerField()
    detalle_factura = models.ForeignKey(Detalle_Factura)
    entregado = models.BooleanField()
#----------------------------------------------------------------------------------------------------

class Remito(models.Model):
    nro_remito = models.IntegerField()
    factura = models.ForeignKey(Factura)
    detalle_remito = models.ForeignKey(Detalle_Remito)
#----------------------------------------------------------------------------------------------------

class Descuento(models.Model):
    fecha = models.datetime
    cantidad = models.IntegerField()
    producto = models.ForeignKey(Producto)
    codigo = models.IntegerField()
#----------------------------------------------------------------------------------------------------

class Donacion(Descuento):
    beneficiario = models.CharField(max_length = 40)
    
    def __unicode__(self):
        return "%s" % self.beneficiario
#----------------------------------------------------------------------------------------------------

class Averia(Descuento):
    pass
#----------------------------------------------------------------------------------------------------

class Extravio(Descuento):
    pass
#----------------------------------------------------------------------------------------------------

class Robo(Descuento):
    pass
#----------------------------------------------------------------------------------------------------