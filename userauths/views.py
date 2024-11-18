from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets , mixins
from rest_framework.filters import OrderingFilter , SearchFilter

from django_filters.rest_framework import DjangoFilterBackend

from .pagination import DefaultPagination
from .models import  User
from .serializers import (
    MyTokenObtainPairSerializer, 
    RegisterSerializer,
    ProfileUserSerializer,
    UserSerializer,
)

import shortuuid

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


def generate_otp():
    uuid_key = shortuuid.uuid()
    unique_key = uuid_key[:6]
    return unique_key


class PasswordChangedView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProfileUserSerializer
    
    def create(self, request, *args, **kwargs):
        payload = request.data

        otp = payload['otp']
        uidb64 = payload['uidb64']

        # Debugging: Print uidb64 value
        print("Received uidb64:", uidb64)
        print("Received otp:", otp)

        try:
            user_id = int(uidb64)

            user = User.objects.get(otp=otp, id=user_id)

            # Change user's password
            password = payload['password']
            user.set_password(password)
            user.otp = ""
            user.save()

            message = {"message": "Password changed successfully"}
            return Response(message, status=status.HTTP_201_CREATED)

        except (User.DoesNotExist, ValueError) as e:
            message = {"message": "User does not exist or invalid identifier"}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        
class ProfileView(APIView):
    permission_classes = (IsAuthenticated , )
    def get(self, request):
        user = request.user
        serializer = ProfileUserSerializer(user)
        return Response(serializer.data)
    
class UserApiView(
                viewsets.GenericViewSet ,
                mixins.ListModelMixin ,
                mixins.RetrieveModelMixin ,
                mixins.CreateModelMixin ,
                mixins.UpdateModelMixin ,
                mixins.DestroyModelMixin ,
                ):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend , SearchFilter, OrderingFilter]
    pagination_class = DefaultPagination
    permission_classes = [IsAuthenticated]
    ordering_fields = ['first_name']
    
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            refresh_token = RefreshToken(refresh_token)
            refresh_token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

