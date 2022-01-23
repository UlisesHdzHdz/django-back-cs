from django.urls import path, re_path
from django.conf.urls import include

from registerUser.views import SaveRegister

urlpatterns = [

    re_path(r'^', SaveRegister.as_view()),
]
