from django.db.models import fields
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from apps.usuarios.models import Usuario

from apps.usuarios.models import Log

from rest_framework.authtoken.models import Token

from datetime import datetime

class RegistrationSerialicer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'cedula', 'mail', 'password', 'password2' ]
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def save(self):
        usuario = Usuario(
                        first_name = self.validated_data["first_name"],
                        last_name = self.validated_data["last_name"],
                        username = self.validated_data["username"],
                        cedula = self.validated_data["cedula"],
                        mail = self.validated_data["mail"],
            )
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password:
            raise serializers.ValidationError({'password': 'Passwords must match.'})

        usuario.set_password(password)
        usuario.save()

        return usuario
    
    def update(self, instance, validated_data):

        instance.first_name = validated_data.get("first_name")
        instance.last_name = validated_data.get("last_name")
        instance.cedula = validated_data.get("cedula")
        instance.mail = validated_data.get("mail")
        instance.password = validated_data.get("password")
        instance.save()
        return instance

class UpdateSerializer(ModelSerializer):

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'cedula', 'mail', 'password' ]
    

class UsuarioSerializer(ModelSerializer):

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'cedula', 'mail', 'password' ]

    def create(self, validated_data):

        user = Usuario(
                        first_name = validated_data.get("first_name"),
                        last_name = validated_data.get("last_name"),
                        username = validated_data.get("username"),
                        cedula = validated_data.get("cedula"),
                        mail = validated_data.get("mail"),
                        password = validated_data.get("password"))
        '''
        user = Usuario.objects.create_user(
                        first_name = validated_data.get("first_name"),
                        last_name = validated_data.get("last_name"),
                        username = validated_data.get("username"),
                        cedula = validated_data.get("cedula"),
                        mail = validated_data.get("mail"),
                        password = validated_data.get("password"))'''
        usuario= user.save()
        #print(usuario)
        data = {}
        data['first_name']=user.first_name
        data['last_name']=user.last_name
        data['username']=user.username
        data['cedula']=user.cedula
        data['mail']=user.mail
        data['password']=user.password
        token = Token.objects.get(user=user).key
        data['token']=token.key
        print(data)
        return user

    def update(self, instance, validated_data):

        instance.first_name = validated_data.get("first_name")
        instance.last_name = validated_data.get("last_name")
        instance.cedula = validated_data.get("cedula")
        instance.mail = validated_data.get("mail")
        instance.password = validated_data.get("password")
        instance.save()
        return instance

class LogSerializer(ModelSerializer):

    class Meta:
        model = Log
        fields = ['id_user', 'timestamp', 'operation']

    def create(self, validated_data):

        log = Log(id_user = validated_data.get("id_user"),
                    operation = validated_data.get("operation"))
        log.save()
        return log