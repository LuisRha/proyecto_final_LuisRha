from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if not user or not user.is_active:
                raise serializers.ValidationError("Invalid credentials")

            # Obtener o crear un token para el usuario
            token, created = Token.objects.get_or_create(user=user)

            # Personalizar el diccionario de retorno con campos adicionales
            user_data = {
                'id': user.id,
                'is_superuser': user.is_superuser,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
            }

            return {
                'user_data': user_data,
                'token': token.key,
            }

        raise serializers.ValidationError("Email and password are required.")
