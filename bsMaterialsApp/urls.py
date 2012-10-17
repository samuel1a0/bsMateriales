from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'bsMaterialsApp.views.login_user'),
    url(r'^login/$', 'bsMaterialsApp.views.login_user'),
    url(r'^deslogear/$', 'bsMaterialsApp.views.deslogear'),
    url(r'^login/menuProd/$', 'bsMaterialsApp.views.menuProducto'),
    url(r'^login/ventaProd$', 'bsMaterialsApp.views.ventaProducto'),
    url(r'^login/menuProd/altaProd$', 'bsMaterialsApp.views.altaProducto'),
    url(r'^login/menuProd/modificacionProd$', 'bsMaterialsApp.views.modificacionProducto'),
    url(r'^login/menuProd/bajaProd$', 'bsMaterialsApp.views.bajaProducto'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/menuProducto/altaProd$', 'bsMaterialsApp.views.altaProducto'),
    
)
if settings.DEBUG and settings.STATIC_ROOT:
    urlpatterns += patterns('',
        (r'%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'), 
            'django.views.static.serve',
            {'document_root' : settings.STATIC_ROOT }),)

