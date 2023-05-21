from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes

from users.serializers import UserProfileSerializer
from users.models import UserProfile
from users.permissions import UpdateOwnProfile
from common.response_helper import responseHelper


class UserProfileView(APIView):
    """User View to handle the user get, update, put and patch"""
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, UpdateOwnProfile, )

    def get_queryset(self):
        """Return queryset filtered by the authenticated user"""
        queryset = UserProfile.objects.filter(id=self.request.user.id)
        return queryset

    def get(self, request: Request, pk: str = None):
        """Endpoint to consume user data"""

        user = self.get_queryset()
        serialized_data = UserProfileSerializer(user, many=True)

        return responseHelper.json_success_response(serialized_data.data[0],
                                                    "Sucesso",
                                                    None)

    def put(self, request: Request, pk: str = None):
        """Endpoint to update the whole user"""

        user = self.get_queryset().first()
        serialized_data = UserProfileSerializer(user, data=request.data)

        if serialized_data.is_valid():
            serialized_data.save()
            return responseHelper.json_success_response(serialized_data.data,
                                                        "Usuário atualizado com sucesso!",
                                                        1)
        else:
            return responseHelper.json_error_response(status.HTTP_400_BAD_REQUEST,
                                                      "Problema ao atualizar usuário!",
                                                      serialized_data.errors)

    def patch(self, request: Request, pk: str = None):
        """Endpoint to partialy update a user"""

        user = self.get_queryset().first()
        serialized_data = UserProfileSerializer(user, data=request.data, partial=True)

        if serialized_data.is_valid():
            serialized_data.save()
            return responseHelper.json_success_response(serialized_data.data,
                                                        "Usuário atualizado com sucesso!",
                                                        1)
        else:
            return responseHelper.json_error_response(status.HTTP_400_BAD_REQUEST,
                                                      "Problema ao atualizar usuário!",
                                                      serialized_data.errors)
        

class UserCreateView(APIView):
    """Class to create new users in the system"""
    permission_classes = (AllowAny, )

    def post(self, request: Request):
        """Endpoint responsable for creating new users"""
        serialized_data = UserProfileSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return responseHelper.json_success_response(serialized_data.data,
                                                        "Usuário criado com sucesso",
                                                        1)
        else:
            return responseHelper.json_error_response(status.HTTP_400_BAD_REQUEST,
                                                      "Erro ao criar novo usuário",
                                                      serialized_data.errors)


class UserLoginAPIView(ObtainAuthToken):
    """Hendle users authentication tokens"""
    permission_classes = (AllowAny, )

    def post(self, request: Request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user: UserProfile = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            response = {
                "email": user.email,
                "name": f"{user.first_name} {user.last_name}",
                "token": token.key
            }
            return responseHelper.json_success_response(response, "Login realizado com sucesso!")

        else:
            return responseHelper.json_error_response(status.HTTP_400_BAD_REQUEST,
                                                      "Problema ao realizar o login",
                                                      serializer.data)
