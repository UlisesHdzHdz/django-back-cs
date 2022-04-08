from rest_framework import routers, serializers, viewsets
# Importacion de modelos
from loadLimage.models import imagentabla


class imagentablaserializer(serializers.ModelSerializer):
    class Meta:
        model = imagentabla
        fields = ('id', 'name_img', 'url_img', 'format_img')
