from django.shortcuts import get_object_or_404
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from app.secretaria.cargo.api.cargo_serializers import CargoSerializer
from app.secretaria.cargo.models import Cargo


class CargoApiViewSet(ModelViewSet):

    serializer_class = CargoSerializer

    @staticmethod
    def handle_exception_response(message, status_code):
        return Response(data={'status': False, 'message': message}, status=status_code)
    """
    Devuelve la información de la tabla cargos.
    @param: request, solicitud HTTP recibida.
    @return: JSON con la información de todos los Cargos.
    """

    def list(self, request, *args, **kwargs):
        try:
            queryset = Cargo.objects.filter(deleted_at=None)
            queryset = self.filter_queryset(queryset)
            serializer = self.get_serializer(queryset, many=True)

            return Response(data={'status': True, 'data': serializer.data}, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return self.handle_exception_response("No se encontraron registros", status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return self.handle_exception_response("Error interno del servidor", status.HTTP_500_INTERNAL_SERVER_ERROR)

    """
    Crea un nuevo registro en la  tabla cargos.
    @param: request, solicitud HTTP recibida.
    @return: JSON con la información de todos los Cargos.
    """

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            cargo = serializer.data
            return Response(data={'status': True, 'message': "Registro creado exitosamente", 'cargo': cargo}, status=status.HTTP_201_CREATED)

        except serializers.ValidationError as e:

            # Validar si el cargo es unico
            if 'cargo' in e.detail:
                for error_detail in e.detail['cargo']:
                    if 'unique' in error_detail.code:
                        print("'unique' presente en e.detail['cargo']")
                        return Response(data={'status': False, 'message': "Ya existe un cargo con este nombre", 'cargo': None}, status=status.HTTP_400_BAD_REQUEST)

            # Otros errores de validación
            return self.handle_exception_response("Error de validación al crear el registro", status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return self.handle_exception_response("Error al crear el registro", status.HTTP_400_BAD_REQUEST)
    """
        Devuelve la información un cargo en espesico de la tabla cargos.
        @param: request, solicitud HTTP recibida.
        @return: JSON con la información de todos los Cargos.
    """

    def retrieve(self, request, *args, **kwargs):

        try:
            instance = Cargo.objects.get(pk=kwargs['pk'], deleted_at=None)

            # Serializar y enviar el registro
            cargo = self.get_serializer(instance).data
            return Response(data={'status': True, 'message': "Cargo Información", 'cargo': cargo}, status=status.HTTP_200_OK)

        except Cargo.DoesNotExist:
            return Response(data={'status': False, 'message': "Cargo Información", 'cargo': ''}, status=status.HTTP_404_NOT_FOUND)

    """
        Actualiza un registro en la  tabla cargos.
        @param: request, solicitud HTTP recibida.
        @return: JSON con la información de todos los Cargos.
    """

    def update(self, request, *args, **kwargs):

        try:

            instance = Cargo.objects.get(pk=kwargs['pk'], deleted_at=None)
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            cargo = self.get_serializer(instance).data
            return Response(data={'status': True, 'message': "Registro actualizado exitosamente", 'cargo': cargo}, status=status.HTTP_200_OK)

        except Http404:
            return self.handle_exception_response("Registro no encontrado", status.HTTP_404_NOT_FOUND)

        except Cargo.DoesNotExist:
            return Response(data={'status': False, 'message': "Cargo Información", 'cargo': ''}, status=status.HTTP_404_NOT_FOUND)

    """
        Elimina lógicamente un registro en la  tabla cargos.
        @param: request, solicitud HTTP recibida.
        @return: JSON con la información de todos los Cargos.
    """

    def destroy(self, request, *args, **kwargs):
        try:
            instance = get_object_or_404(
                Cargo, pk=kwargs['pk'], deleted_at=None)

            # Guardar la información del registro antes de eliminarlo
            deleted_data = CargoSerializer(instance).data

            instance.deleted_at = timezone.now()
            instance.save()

            return Response(data={'status': True, 'message': "Registro eliminado exitosamente", 'cargo': deleted_data}, status=status.HTTP_200_OK)

        except Http404:
            return Response(data={'status': False, 'message': "Registro no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Puedes ajustar el manejo de otras excepciones según tus necesidades
            return Response(data={'status': False, 'message': "Error al eliminar el registro: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
