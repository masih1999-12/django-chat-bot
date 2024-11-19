from django.db import models

class Chat(models.Model):
    request_text=models.CharField(max_length=255)
    response_text=models.CharField(max_length=255)