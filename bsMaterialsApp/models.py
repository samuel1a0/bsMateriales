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
    descripcion = models.CharField(max_length = 40, blank = True)
    tipoProducto = models.ForeignKey(TipoProducto)
    
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
    direccion = models.CharField(max_length = 40)
    telefono = models.CharField(max_length = 15)
    rubro = models.ForeignKey(Rubro)
    
    def __unicode__(self):
        return "%s" % self.rubro
#---------------------------------------------------------------------------------------------------

class Stock(models.Model):
    reservadosConfirmados = models.IntegerField()
    reservadosNoConfirmados = models.IntegerField()
    deposito = models.ForeignKey(Deposito)
    producto = models.ForeignKey(Producto)
    
    def __unicode__(self):
        return "%s" % self.nombre
#---------------------------------------------------------------------------------------------------

class Detalle(models.Model):
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()
    producto = models.ForeignKey(Producto)
#----------------------------------------------------------------------------------------------------

class DetalleNotaVenta(Detalle):
    nota = models.ForeignKey('NotaVenta')
    pass
#----------------------------------------------------------------------------------------------------

class DetalleFactura(Detalle):
    factura = models.ForeignKey('Factura')
    venta = models.ForeignKey(DetalleNotaVenta)
    pass
#----------------------------------------------------------------------------------------------------

class NotaVenta(models.Model):
    nroNota = models.IntegerField()
    nombre_cliente = models.CharField(max_length = 40)
    apellido_cliente = models.CharField(max_length = 20)
    fecha = models.datetime    
#----------------------------------------------------------------------------------------------------

class Factura(models.Model):
    nroFactura = models.IntegerField()
    fecha = models.datetime
    formaDePago = models.CharField(max_length = 15)
    precioTotal = models.IntegerField()
    ventaNota = models.ForeignKey(NotaVenta)
    factura = models.ForeignKey('Remito')    
#----------------------------------------------------------------------------------------------------

class Remito(models.Model):
    nroRemito = models.IntegerField()
#----------------------------------------------------------------------------------------------------

class DetalleRemito(models.Model):
    cantidad = models.IntegerField()
    entregado = models.BooleanField()
    detalleFactura = models.ForeignKey(DetalleFactura)
    remito = models.ForeignKey(Remito)
#----------------------------------------------------------------------------------------------------

class Descuento(models.Model):
    nroDescuento = models.IntegerField()
    fecha = models.datetime
    cantidad = models.IntegerField()
    producto = models.ForeignKey(Producto)
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