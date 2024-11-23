from django.db import models

class Chat(models.Model):
    request_text=models.TextField()
    response_text=models.TextField()