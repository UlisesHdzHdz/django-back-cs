from django.shortcuts import render

# Create your views here.
# 1.2 urls_hijo
from multiprocessing import context
from django.http import request
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Importacion de modelos
from loadLimage.models import imagentabla
import json

# Importaciones de serializadores
from loadLimage.serializers import imagentablaserializer

# Create your views here.


class imagentablalist(APIView):

    def jsonList(self, message, data, status):
        jsonok = {"messages": message, "pay_load": data, "status": status}
        contenido = json.dumps(jsonok)
        responseok = json.loads(contenido)
        return responseok

    # Metodo para obtener la lista de registro
    def get(self, request, format=None):
        queryset = imagentabla.objects.all()
        serializer = imagentablaserializer(
            queryset, many=True, context={'request': request})
      
        responseok = self.jsonList(
            "succes", serializer.data, status.HTTP_200_OK)
        return Response(responseok)

    # Metodo para crear un nuevo registro
    def post(self, request, format=None):
        serializer = imagentablaserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
          
           
            responseok = self.jsonList(
                "succes", serializer.data, status.HTTP_201_CREATED)
            return Response(responseok)
        responseok = self.jsonList(
            "error", serializer.errors, status.HTTP_400_BAD_REQUEST)
        return Response(responseok)


class imagentabladetail(APIView):
    def jsonList2(self, message, data, status):
        jsonok = {"messages": message, "pay_load": data, "status": status}
        contenido = json.dumps(jsonok)
        responseok = json.loads(contenido)
        return responseok

    # Metodo para consultar el id y me retorne si exite o no existe
    def get_object(self, pk):
        try:
            return imagentabla.objects.get(pk=pk)
        except imagentabla.DoesNotExist:
            return 0

    # Metodo para consultar el id y retornar los valores y sus campos
    def get(self, request, pk, format=None):
        print("id de la consulta : "+pk)
        idresponse = self.get_object(pk)
        if idresponse != 0:
            idresponse = imagentablaserializer(idresponse)
            responseok = self.jsonList2(
                "succes", idresponse.data, status.HTTP_200_OK)
            return Response(responseok)
        return Response("no hay datos aaaa", status=status.HTTP_400_BAD_REQUEST)

 # Metodo para consultar el id y actualizar los valores de sus campos

    def put(self, request, pk, format=None):
        idresponse = self.get_object(pk)
        serializer = imagentablaserializer(idresponse, data=request.data)
        if serializer.is_valid():
            serializer.save()
            responseok = self.jsonList2(
                "succes", serializer.data, status.HTTP_200_OK)
            return Response(responseok)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Metodo para consultar id y eliminar el registro

    def delete(self, request, pk, format=None):
        objetive = self.get_object(pk)
        if objetive != "No existe":
            objetive.delete()
            return Response("Dato eliminado", status=status.HTTP_200_OK)
        else:
            return Response("Dato no encontrado", status=status.HTTP_400_BAD_REQUEST)
