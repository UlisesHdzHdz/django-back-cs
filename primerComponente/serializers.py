# 1.1 views
from rest_framework import routers, serializers, viewsets
# Importacion de modelos
from primerComponente.models import primertabla


class primertablaserializer(serializers.ModelSerializer):
    class Meta:
        model = primertabla
        fields = ('id', 'nombre', 'edad')
