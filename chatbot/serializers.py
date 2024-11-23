from rest_framework import serializers
# from .model_loader import falcon_model
from .models import Chat

class ChatSerializer(serializers.Serializer):
    request_text=serializers.CharField()