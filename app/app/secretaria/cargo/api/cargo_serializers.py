from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from app.secretaria.cargo.models import Cargo


class CargoSerializer(serializers.ModelSerializer):
    cargo = serializers.CharField(
        max_length=255,
        validators=[UniqueValidator(queryset=Cargo.objects.all())]
    )

    class Meta:
        model = Cargo
        fields = ['id','cargo', 'descripcion',
                  'created_at', 'updated_at', 'deleted_at']
        read_only_fields = ['created_at', 'updated_at', 'deleted_at']
