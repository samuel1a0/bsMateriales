# Create your views here.
#*-*coding: utf-8 --*-*
from django.contrib.auth import logout
from django.template import RequestContext
from django.shortcuts import render_to_response
from bsMaterialsApp.models import Producto, TipoProducto
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

#import ipdb
#ipdb.set_trace()
def login_user(request):
    state = "Por favor iniciar sesion para poder continuar..."
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

#@login_required(redirect_field_name=, login_url)
@login_required(login_url='/')
def deslogear(request):
    logout(request)
    return render_to_response('login.html', RequestContext(request, {}))
    
def indexLogin(request):
    return render_to_response('login.html', RequestContext(request, {}))

@login_required(login_url='/')
def menuProducto(request):
    return render_to_response('gestionProd.html',{'usuario':request.user.username}, RequestContext(request, {}))

@login_required(login_url='/')
def ventaProducto(request):
    productos =  Producto.objects.all()
    return render_to_response('ventaProd.html',{'productos': productos,}, RequestContext(request, {}))

@login_required(login_url='/')
def modificacionProducto(request):
    return render_to_response('modificacionProd.html', RequestContext(request, {}))


@login_required(login_url='/')
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
        return render_to_response('altaProd.html',{'estado':estado, 'tipoProductos': tipoProductos, 'usuario': request.user.username}, RequestContext(request, {}))
@login_required(login_url='/')
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
