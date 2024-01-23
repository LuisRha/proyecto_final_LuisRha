from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from .user_serializers import UserLoginSerializer


class UserLoginAPIView(ObtainAuthToken):

    """
    Iniciar sesión o generar un token.
    @param: request, solicitud HTTP recibida.
    @return: JSON con la información del token.
    """

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():

            data = serializer.validated_data

            user = data['user_data']
            token = data['token']

            return Response({
                'status': True,
                'user': user,
                'accessToken': token,
            }, status=status.HTTP_200_OK)

        return Response({'status': False, 'message': 'Invalid input'}, status=status.HTTP_400_BAD_REQUEST)
