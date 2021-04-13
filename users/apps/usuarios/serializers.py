from rest_framework.serializers import ModelSerializer

from apps.usuarios.models import Usuario

from apps.usuarios.models import Log

from datetime import datetime

class UsuarioSerializer(ModelSerializer):

    class Meta:
        model = Usuario
        fields = ['id', 'first_name', 'last_name', 'cedula', 'mail', 'password' ]

    def create(self, validated_data):

        user = Usuario(first_name = validated_data.get("first_name"),
                        last_name = validated_data.get("last_name"),
                        cedula = validated_data.get("cedula"),
                        mail = validated_data.get("mail"),
                        password = validated_data.get("password"))
        user.save()
        return user

    def update(self, instance, validated_data):

        instance.first_name = validated_data.get("first_name"),
        instance.last_name = validated_data.get("last_name"),
        #instance.cedula = validated_data.get("cedula"),
        instance.mail = validated_data.get("mail"),
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