# Generated by Django 5.1.3 on 2024-11-19 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0009_alter_user_managers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='otp',
        ),
    ]
