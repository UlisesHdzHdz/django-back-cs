from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
import os
import datetime
from Profile.models import Profile
from django.contrib.auth.models import User
from Profile.serializers import ProfileSerializer


class ProfileTable(APIView):

    def get_objectUser(self, iduser):
        try:
            return User.objects.get(pk=iduser)
        except User.DoesNotExist:
            return 404

    def post(self, request):
     
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            img = Profile(**validated_data)
            img.save()
            serializer_response = ProfileSerializer(img)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response("Este usuario tiene un perfil existente", status=status.HTTP_400_BAD_REQUEST)


class ProfileTableDetail(APIView):
    def get_object(self, pk):
        try:
            return Profile.objects.get(id_user=pk)
        except Profile.DoesNotExist:
            return 404

    def res_custom(self, user, data, status):
        response = {
            "first_name": user[0]['first_name'],
            "last_name": user[0]['last_name'],
            "username": user[0]['username'],
            "email": user[0]['email'],
            "id_user": data.get('id_user'),
            "url_img": data.get('url_img'),
        }
        return response

    def get(self, request, pk, format=None):
        idresponse = self.get_object(pk)
        if idresponse != 404:
            idresponse = ProfileSerializer(idresponse)
            user = User.objects.filter(id=pk).values()
            responseok = self.res_custom(
                user, idresponse.data, status.HTTP_200_OK)
            return Response(responseok)
        return Response("No hay datos", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):

        archivos = request.data['url_img']
        idresponse = self.get_object(pk)
        if(idresponse != 404):
            serializer = ProfileSerializer(idresponse)
            try:
                os.remove('assets/'+str(idresponse.url_img))
            except os.error:
                print("La imagen no existe")
            idresponse.url_img = archivos
            idresponse.save()
            responsedata = {
                'mensaje': 'Request exitoso',
                'url_img': serializer.data['url_img'],
            }
            return Response(responsedata, status.HTTP_201_CREATED)
        else:
            return Response("Request fallido", status=status.HTTP_400_BAD_REQUEST)


class UserProfile(APIView):

    def res_custom(self, user, status):
        response = {
            "first_name": user[0]['first_name'],
            "last_name": user[0]['last_name'],
            "username": user[0]['username'],
            "email": user[0]['email']
        }
        return response

    def get(self, request, pk, format=None):
        idresponse = User.objects.filter(id=pk).values()
        if(idresponse != 404):
            responsedata = self.res_custom(idresponse, status.HTTP_200_OK)
            return Response(responsedata)
        return("Usuario no encontrado")

    def put(self, request, pk, format=None):
        data = request.data
        user = User.objects.filter(id=pk)
        user.update(username=data.get('username'))
        user.update(first_name=data.get('first_name'))
        user.update(last_name=data.get('last_name'))
        user.update(email=data.get('email'))
        user2 = User.objects.filter(id=pk).values()
        return Response(self.res_custom(user2, status.HTTP_200_OK))
