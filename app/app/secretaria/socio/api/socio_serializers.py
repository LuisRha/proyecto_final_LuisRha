from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from app.secretaria.cargo.models import Cargo
from app.secretaria.socio.models import Socio


class SocioSerializer(serializers.ModelSerializer):

    cedula = serializers.CharField(
        max_length=15,
        validators=[UniqueValidator(queryset=Socio.objects.all())]
    )

    nombres = serializers.CharField(max_length=255)
    apellidos = serializers.CharField(max_length=255)
    telefono = serializers.CharField(
        max_length=20, allow_blank=True, allow_null=True)
    correo = serializers.EmailField(allow_blank=True, allow_null=True)
    direccion = serializers.CharField(
        max_length=255, allow_blank=True, allow_null=True)
    fecha_nacimiento = serializers.DateField()
    cargo = serializers.PrimaryKeyRelatedField(queryset=Cargo.objects.all())

    class Meta:
        model = Socio
        fields = ['id','cedula', 'nombres', 'apellidos', 'telefono', 'correo', 'direccion',
                  'fecha_nacimiento', 'cargo', 'created_at', 'updated_at', 'deleted_at']
        read_only_fields = ['created_at', 'updated_at', 'deleted_at']
