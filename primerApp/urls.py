
from django.urls import path, include, re_path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
# Serializers define the API representation.
#import Register
from registerUser.views import RegistroView


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

# 1.4 Agregamos los los urls_hijos al url_padre de los componentes creados
# urlpatterns = [
#     path('', include(router.urls)),
#     # re_path(r'^api/v1/registerUser', include('registerUser.urls')),
#     re_path(r'^api/', include('loginComponente.urls')),xx
#     re_path(r'^api/v1/user/', include('Profile.urls')),xx
#     re_path(r'^api/v1/create_user', RegistroView.as_view(), name='create_user'),xx
#     re_path(r'^api/v1/primerComponente/', include('primerComponente.urls')),xx
#     re_path(r'^api/v1/loadLimage/', include('loadLimage.urls')),xx
#     re_path(r'assets/(?P<path>.*)$', serve,
#             {'document_root': settings.MEDIA_ROOT}),xx
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))xx
# ]

urlpatterns = [
    path('', include(router.urls)),
    #URL de registro
    re_path(r'^api/v1/create_user', RegistroView.as_view(), name='create_user'),
    re_path(r'^api/', include('loginComponente.urls')),
    re_path(r'^api/v1/user/', include('Profile.urls')),
    re_path(r'^api/v1/load_image/', include('loadLimage.urls')),
    re_path(r'^api/v1/primer_componente/', include('primerComponente.urls')),
    re_path(r'assets/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
