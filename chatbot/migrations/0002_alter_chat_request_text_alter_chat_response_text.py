# Generated by Django 5.1.3 on 2024-11-23 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='request_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='chat',
            name='response_text',
            field=models.TextField(),
        ),
    ]
