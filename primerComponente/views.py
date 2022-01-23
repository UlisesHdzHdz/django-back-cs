# 1.2 urls_hijo
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Importacion de modelos
from primerComponente.models import primerTabla

# Importaciones de serializadores
from primerComponente.serializers import primerTablaSerializer

# Create your views here.
class primerTablaList(APIView):
    def get(self, request,format=None):
        queryset = primerTabla.objects.all()
        serializers = primerTablaSerializer(queryset,many=True,context={'request':request})
        return Response(serializers.data)