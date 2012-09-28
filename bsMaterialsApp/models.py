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
    unidadMedida = models.CharField(max_length = 40)
    descripcion = models.CharField(max_length = 40, blank=True)
    rubro = models.ForeignKey(Rubro)
    
    def __unicode__(self):
        return "%s" % self.nombre
#---------------------------------------------------------------------------------------------------

class Producto(models.Model):
    nombre = models.CharField(max_length = 40)
    stockTotal = models.IntegerField()
    tipoProducto = models.ForeignKey(TipoProducto)
    descripcion = models.CharField(max_length = 40, blank = True)
    
    def __unicode__(self):
        return "%s" % self.nombre
#---------------------------------------------------------------------------------------------------

class Fraccionable(Producto):
    medida = models.CharField(max_length = 40)
#---------------------------------------------------------------------------------------------------

class NoFraccionable(Producto):
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
    subtotal = models.IntegerField()
    producto = models.ForeignKey(Producto)
#----------------------------------------------------------------------------------------------------

class DetalleNotaVenta(Detalle):
    pass
#----------------------------------------------------------------------------------------------------

class DetalleFactura(Detalle):
    venta = models.ForeignKey(DetalleNotaVenta)
    pass
#----------------------------------------------------------------------------------------------------

class NotaVenta(models.Model):
    nroNota = models.IntegerField()
    nombre_cliente = models.CharField(max_length = 40)
    apellido_cliente = models.CharField(max_length = 20)
    fecha = models.datetime    
    detalle = models.ForeignKey(DetalleNotaVenta)
#----------------------------------------------------------------------------------------------------

class Factura(models.Model):
    nroFactura = models.IntegerField()
    fecha = models.datetime
    formaDePago = models.CharField(max_length = 15)
    precioTotal = models.IntegerField()
    ventaNota = models.ForeignKey(NotaVenta)
    detalle = models.ForeignKey(DetalleFactura)    
#----------------------------------------------------------------------------------------------------

class DetalleRemito(models.Model):
    producto = models.ForeignKey(Producto)
    cantidad = models.IntegerField()
    detalleFactura = models.ForeignKey(DetalleFactura)
    entregado = models.BooleanField()
#----------------------------------------------------------------------------------------------------

class Remito(models.Model):
    nroRemito = models.IntegerField()
    factura = models.ForeignKey(Factura)
    detalleRemito = models.ForeignKey(DetalleRemito)
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