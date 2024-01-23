from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import serializers, status, viewsets
from rest_framework.response import Response

from app.secretaria.socio.api.socio_serializers import SocioSerializer
from app.secretaria.socio.models import Socio


class SocioViewSet(viewsets.ModelViewSet):
    serializer_class = SocioSerializer

    @staticmethod
    def handle_exception_response(message, status_code):
        return Response(data={'status': False, 'message': message}, status=status_code)

    """
    Devuelve la información de la tabla socios.
    @param: request, solicitud HTTP recibida.
    @return: JSON con la información de todos los Socios.
    """

    def list(self, request, *args, **kwargs):
        try:
            queryset = Socio.objects.filter(deleted_at=None)
            queryset = self.filter_queryset(queryset)
            serializer = self.get_serializer(queryset, many=True)

            return Response(data={'status': True, 'data': serializer.data}, status=status.HTTP_200_OK)

        except Socio.DoesNotExist:
            return self.handle_exception_response("No se encontraron registros", status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return self.handle_exception_response("Error interno del servidor", status.HTTP_500_INTERNAL_SERVER_ERROR)

    """
    Crea un nuevo registro en la tabla socios.
    @param: request, solicitud HTTP recibida.
    @return: JSON con la información de todos los Socios.
    """

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            socio = serializer.data
            print ('socio')
            print(socio)
            return Response(data={'status': True, 'message': "Registro creado exitosamente", 'socio': socio}, status=status.HTTP_201_CREATED)

        except serializers.ValidationError as e:
            print ('ValidationError', e.detail)
            # Validar si el socio es unico
            if 'cedula' in e.detail:
                for error_detail in e.detail['cedula']:
                    if 'unique' in error_detail.code:
                        print("'unique' presente en e.detail['cedula']")
                        return Response(data={'status': False, 'message': "Ya existe un socio con esta cédula", 'cedula': None}, status=status.HTTP_400_BAD_REQUEST)
                    
            return self.handle_exception_response(data={'status': True, 'error': e.detail, 'msg': 'Error de validación al crear el registro'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return self.handle_exception_response("Error al crear el registro", status.HTTP_400_BAD_REQUEST)

    """
    Devuelve la información de un socio específico de la tabla socios.
    @param: request, solicitud HTTP recibida.
    @return: JSON con la información de un Socio.
    """

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = Socio.objects.get(pk=kwargs['pk'], deleted_at=None)
            socio = self.get_serializer(instance).data
            return Response(data={'status': True, 'message': "Socio Información", 'socio': socio}, status=status.HTTP_200_OK)

        except Socio.DoesNotExist:
            return Response(data={'status': False, 'message': "Socio no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    """
    Actualiza un registro en la tabla socios.
    @param: request, solicitud HTTP recibida.
    @return: JSON con la información de un Socio.
    """

    def update(self, request, *args, **kwargs):
        try:
            instance = Socio.objects.get(pk=kwargs['pk'], deleted_at=None)
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            socio = self.get_serializer(instance).data
            return Response(data={'status': True, 'message': "Registro actualizado exitosamente", 'socio': socio}, status=status.HTTP_200_OK)

        except Socio.DoesNotExist:
            return Response(data={'status': False, 'message': "Socio no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    """
    Elimina lógicamente un registro en la tabla socios.
    @param: request, solicitud HTTP recibida.
    @return: JSON con la información de un Socio eliminado.
    """

    def destroy(self, request, *args, **kwargs):
        try:
            instance = get_object_or_404(
                Socio, pk=kwargs['pk'], deleted_at=None)

            deleted_data = SocioSerializer(instance).data

            instance.deleted_at = timezone.now()
            instance.save()

            return Response(data={'status': True, 'message': "Registro eliminado exitosamente", 'socio': deleted_data}, status=status.HTTP_200_OK)

        except Http404:
            return Response(data={'status': False, 'message': "Registro no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response(data={'status': False, 'message': f"Error al eliminar el registro: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
