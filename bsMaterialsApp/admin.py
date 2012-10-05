from django.contrib import admin
from bsMaterialsApp.models import NotaVenta, DetalleNotaVenta, TipoProducto,Producto, Rubro 

admin.site.register(Producto)
admin.site.register(TipoProducto)
admin.site.register(Rubro)

class DetalleNotaVentaInline(admin.TabularInline):
    model = DetalleNotaVenta
     
class VentaAdmin(admin.ModelAdmin):
    inlines = [DetalleNotaVentaInline]

admin.site.register(NotaVenta, VentaAdmin)