from django.urls import path, re_path
from django.conf.urls import include

from loadLimage.views import imagentablalist
from loadLimage.views import imagentabladetail


urlpatterns = [
    re_path(r'^listaImagen/$', imagentablalist.as_view()),
    re_path(r'^listaImagen/(?P<pk>\d+)$', imagentabladetail.as_view()),

]
