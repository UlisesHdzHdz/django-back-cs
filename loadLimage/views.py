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
from loadLimage.models import imagenTabla
import json

# Importaciones de serializadores
from loadLimage.serializers import imagenTablaSerializer

# Create your views here.


class imagenTablaList(APIView):

    def jsonList(self, message, data, status):
        structJ = {"messages": message, "pay_load": data, "status": status}
        contenido = json.dumps(structJ)
        responseOk = json.loads(contenido)
        return responseOk

    # Metodo para obtener la lista de registro
    def get(self, request, format=None):
        queryset = imagenTabla.objects.all()
        serializer = imagenTablaSerializer(
            queryset, many=True, context={'request': request})
        # return Response(serializer.data)
        responseOk = self.jsonList(
            "succes", serializer.data, status.HTTP_200_OK)
        return Response(responseOk)

    # Metodo para crear un nuevo registro
    def post(self, request, format=None):
        serializer = imagenTablaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            # return Response(datas, status=status.HTTP_201_CREATED)
            responseOk = self.jsonList(
                "succes", serializer.data, status.HTTP_201_CREATED)
            return Response(responseOk)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        responseOk = self.jsonList(
            "error", serializer.errors, status.HTTP_400_BAD_REQUEST)
        return Response(responseOk)


class imagenTablaDetail(APIView):
    def jsonList2(self, message, data, status):
        structJ = {"messages": message, "pay_load": data, "status": status}
        contenido = json.dumps(structJ)
        responseOk = json.loads(contenido)
        return responseOk

    # Metodo para consultar el id y me retorne si exite o no existe
    def get_object(self, pk):
        try:
            return imagenTabla.objects.get(pk=pk)
        except imagenTabla.DoesNotExist:
            return 0

    # Metodo para consultar el id y retornar los valores y sus campos
    def get(self, request, pk, format=None):
        print("id de la consulta : "+pk)
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse = imagenTablaSerializer(idResponse)
            # return Response(idResponse.data, status=status.HTTP_200_OK)
            responseOk = self.jsonList2(
                "succes", idResponse.data, status.HTTP_200_OK)
            return Response(responseOk)
        return Response("no hay datos aaaa", status=status.HTTP_400_BAD_REQUEST)

 # Metodo para consultar el id y actualizar los valores de sus campos

    def put(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        serializer = imagenTablaSerializer(idResponse, data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            # return Response(datas, status=status.HTTP_200_OK)
            responseOk = self.jsonList2(
                "succes", serializer.data, status.HTTP_200_OK)
            return Response(responseOk)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Metodo para consultar id y eliminar el registro

    def delete(self, request, pk, format=None):
        objetive = self.get_object(pk)
        if objetive != "No existe":
            objetive.delete()
            return Response("Dato eliminado", status=status.HTTP_200_OK)
        else:
            return Response("Dato no encontrado", status=status.HTTP_400_BAD_REQUEST)
