# 1.3 urls_padre
from django.urls import path, re_path
from django.conf.urls import include

from primerComponente.views import primertablalist
from primerComponente.views import primertabladetail
urlpatterns = [
    re_path(r'^lista/$', primertablalist.as_view()),
    re_path(r'^lista/(?P<pk>\d+)$', primertabladetail.as_view()),

]
