from django.urls import path, re_path
from django.conf.urls import include

from loadLimage.views import imagenTablaList
from loadLimage.views import imagenTablaDetail


urlpatterns = [
    re_path(r'^listaImagen/$', imagenTablaList.as_view()),
    re_path(r'^listaImagen/(?P<pk>\d+)$', imagenTablaDetail.as_view()),

]
