from django.urls import path, re_path
from django.conf.urls import include
from rest_framework_simplejwt.views import TokenRefreshView
from loginComponente.views import LoginAuth, MyObtainTokenPairView

urlpatterns = [
    # re_path(r'^', LoginAuth.as_view()),
    re_path(r'^v1/Login', LoginAuth.as_view()),
    re_path(r'^v2/Login', MyObtainTokenPairView.as_view()),
    re_path(r'^v1/Refresh', TokenRefreshView.as_view()),
]
