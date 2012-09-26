# Create your views here.
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response
from bsMaterialsApp.models import Producto, TipoProducto
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


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
                state = "You're successfully logged in!"
                return render_to_response('MenuGerente.html',{'usuario':username}, context_instance=RequestContext(request))
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
            
        return render_to_response('index.html',{'estado':state},context_instance=RequestContext(request))    



def index(request):
    return render_to_response('index.html', RequestContext(request, {}))

def menuProd(request):
    return render_to_response('GestionProductos.html', RequestContext(request, {}))



def altaProd(request):
    producto = Producto()
    tipoProductos = TipoProducto.objects.all()
    estado = ''
    if request.POST:
         producto.nombre= request.POST.get('nombre')
         producto.stockT= request.POST.get('stock')
         producto.descripcion=request.POST.get('descripcion')
         producto.save()
         estado='ALTA PRODUCTO: '+producto.nombre+''

    #return login_required()
    return render_to_response('altaProd.html',{'estado':estado, 'tipoProductos': tipoProductos}, RequestContext(request, {}))

        

