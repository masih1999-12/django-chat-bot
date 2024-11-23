from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter , SearchFilter
from rest_framework import  viewsets , mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from .model_loader import run_ollama
from .models import Chat
from .serializers import ChatSerializer

class ChatApiView(
                viewsets.GenericViewSet,
                mixins.CreateModelMixin,
                ):
    queryset=Chat.objects.none()
    serializer_class=ChatSerializer
    def create(self, request, *args, **kwargs):
        serializer:ChatSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request_text = serializer.validated_data['request_text']
        if not request_text:
            return Response({"error": "request_text is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        response = run_ollama(request_text)
        chat=Chat.objects.create(request_text=request_text,response_text=response)
        headers = self.get_success_headers(serializer.data)

        return Response({'id':chat.id,'response_text':chat.response_text}, status=status.HTTP_201_CREATED, headers=headers)