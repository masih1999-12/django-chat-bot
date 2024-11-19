from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter , SearchFilter
from rest_framework import  viewsets , mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Chat
from .serializers import ChatSerializer

class ChatApiView(
                viewsets.GenericViewSet,
                mixins.CreateModelMixin,
                ):
    queryset=Chat.objects.none()
    serializer_class=ChatSerializer
    