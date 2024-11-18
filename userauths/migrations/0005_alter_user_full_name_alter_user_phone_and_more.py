# Generated by Django 4.2.14 on 2024-08-08 01:19

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0004_remove_user_permissions_role_user_rols'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(default='admin user', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]