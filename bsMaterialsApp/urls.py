from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'bsMaterialsApp.views.index'),
    url(r'^login/$', 'bsMaterialsApp.views.login_user'),
    url(r'^login/menuProd/$', 'bsMaterialsApp.views.menuProd'),
    url(r'^login/ventaProd$', 'bsMaterialsApp.views.ventProd'),
    url(r'^login/menuProd/altaProd$', 'bsMaterialsApp.views.altaProd'),
    url(r'^login/menuProd/modificacionProd$', 'bsMaterialsApp.views.modificacionProd'),
    url(r'^login/menuProd/bajaProd$', 'bsMaterialsApp.views.bajaProd'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/menuProducto/altaProd$', 'bsMaterialsApp.views.altaProd'),
    
)
if settings.DEBUG and settings.STATIC_ROOT:
    urlpatterns += patterns('',
        (r'%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'), 
            'django.views.static.serve',
            {'document_root' : settings.STATIC_ROOT }),)

