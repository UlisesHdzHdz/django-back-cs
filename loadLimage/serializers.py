from rest_framework import routers, serializers, viewsets
# Importacion de modelos
from loadLimage.models import imagenTabla


class imagenTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = imagenTabla
        fields = ('id', 'name_img', 'url_img', 'format_img')
