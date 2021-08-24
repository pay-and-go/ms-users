from django.shortcuts import render
from apps.usuarios.serializers import UsuarioSerializer
from apps.usuarios.serializers import RegistrationSerialicer
from apps.usuarios.serializers import UpdateSerializer
from apps.usuarios.serializers import LogSerializer
from apps.usuarios.models import Usuario
from apps.usuarios.models import Log
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
# Create your views here.
@api_view(['POST',])
@permission_classes((AllowAny,))
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerialicer(data=request.data)
        data = {}
        if serializer.is_valid():
            usuario = serializer.save()
            data['response'] = "succesfully registered a new user."
            data['email'] = usuario.mail
            data['username'] = usuario.username
            token = Token.objects.get(user=usuario).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)

@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def detail_view(request, username):
    try:
        usu=Usuario.objects.get(mail=username)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = RegistrationSerialicer(usu)
        return Response(serializer.data)

@api_view(['PUT',])
@permission_classes((IsAuthenticated,))
def update_view(request, username):
    try:
        usu=Usuario.objects.get(mail=username)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        serializer = UpdateSerializer(usu, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"]= "update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
@permission_classes((IsAuthenticated,))
def delete_view(request, username):
    try:
        usu=Usuario.objects.get(mail=username)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        operation= usu.delete()
        data = {}
        if operation:
            data["success"]="delete successful"
        else:
            data["failure"]="delete failed"
        return Response(data=data)


class UserList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        print(token)
        return self.create(request, *args, **kwargs)

class UserDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class LogList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = Log.objects.all()
    serializer_class = LogSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)