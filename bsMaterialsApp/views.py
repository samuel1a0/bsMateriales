# Create your views here.
#*-*coding: utf-8 --*-*
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response
from bsMaterialsApp.models import Producto, TipoProducto
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "Exito!"
                return render_to_response('menuGerente.html',{'usuario':username,'contraseña':password}, context_instance=RequestContext(request))
            else:
                state = "Cuenta Inactiva"
        else:
            state = " nombre de usuario o contraseña incorrecta."
            
        return render_to_response('login.html',{'estado':state},context_instance=RequestContext(request))    



def indexLogin(request):
    return render_to_response('login.html', RequestContext(request, {}))

def menuProducto(request):
    return render_to_response('gestionProd.html', RequestContext(request, {}))

def ventaProducto(request):
    productos =  Producto.objects.all()
    return render_to_response('ventaProd.html',{'productos': productos,}, RequestContext(request, {}))

def modificacionProducto(request):
    productos = Producto.objects.all()
    return render_to_response('modificacionProd.html',{'productos':productos}, RequestContext(request, {}))

def altaProducto(request):
    producto = Producto()
    tipoProductos = TipoProducto.objects.all()
    estado = ''
    if request.POST:
         producto.nombre= request.POST.get('nombre')
         producto.stockTotal= request.POST.get('stock')
         producto.descripcion=request.POST.get('descripcion')
         producto.tipoProducto=TipoProducto.objects.get(pk= request.POST.get('tipoProducto'))
         producto.save()
         estado='ALTA PRODUCTO: '+producto.nombre+''

    #return login_required()
    return render_to_response('altaProd.html',{'estado':estado, 'tipoProductos': tipoProductos}, RequestContext(request, {}))

def bajaProducto(request):
    producto = Producto()
    estado = ""
    if request.POST:
        nombreProducto = request.POST.get('nombre')
        try:
            producto = Producto.objects.get(nombre= nombreProducto)
            producto.delete()
            estado = "El producto "+nombreProducto+" ha sido dado de baja"
        except ObjectDoesNotExist:
            estado = "no existe el producto: "+nombreProducto
    return render_to_response('bajaProd.html',{'estado':estado}, RequestContext(request, {}))
