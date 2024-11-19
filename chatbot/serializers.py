from rest_framework import serializers

from .models import Chat

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chat
        fields=('id','request_text','response_text',)
    def get_fields(self):
        fields=super().get_fields()
        if self.context['request'].method == 'POST':
            fields=dict()
            fields['request_text'] = serializers.CharField()
        return fields
    def create(self, validated_data):
        chat=Chat.objects.create(request_text=validated_data['request_text'],response_text='hi')
        return chat