from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from auth.user.models import User
from auth.user.api.user_serializers import UserAddSerializer

class UsersView(APIView):

    """
    * Display all data
    * @return response data
    """
    def get(self, request):

        try:
            data = User.objects.all()
            users = UserAddSerializer(data, many=True)

            if len(data)>0:
                return Response(status=status.HTTP_200_OK, data=users.data)

            return Response(status=status.HTTP_204, data=users.data)
            
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserAddView(APIView):
    """
    * Store new element
    * @param request
    * @return response data
    """
    def post(self, request):

        try:
            data = UserAddSerializer(data=request.data)

            if data.is_valid(raise_exception=True):
                data.save()
                return Response(status=status.HTTP_200_OK, data={'status': True})

            return Response(status=status.HTTP_400_BAD_REQUEST, data=data.errors)

        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserShowView(APIView):
    """
    * Display specified data
    * @param id
    * @return response item
    """
    def show(self, request, id):

        try:
            item = User.objects.filter(id=id)
            users = UserAddSerializer(data, many=True)

            if len(item)>0:
                return Response(status=status.HTTP_200_OK, data=users.data)

            return Response(status=status.HTTP_204, data=users.data)
            
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserUpdateView(APIView):
    """
    * Update  element
    * @param  request
    * @param  user
    * @return response data
    """
    def put(self, request, id):

        try:
            user = User.objects.get(id=id)
            data = UserAddSerializer(recouserrd, data=request.data)

            if data.is_valid(raise_exception=True):
                data.save()
                return Response(data.data, status=status.HTTP_200_OK)
            
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            return Response("Registro no encontrado", status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    """
    * Delete  element
    * @param  id
    * @return response data
    """
    def delete(id):
        try:
            user = User.objects.get(id=id)
            user.delete()

            return Response(data={'status': True, 'sms':"Registro eliminado exitosamente"}, status=status.HTTP_204_NO_CONTENT)

        except User.DoesNotExist:
            return Response(data={'status': True, 'sms':"El registro no existe"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)