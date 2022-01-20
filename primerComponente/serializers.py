# 1.1 views
from rest_framework import routers, serializers, viewsets
# Importacion de modelos
from primerComponente.models import PrimerTabla

class primerTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimerTabla
        fields = ('nombre', 'edad')