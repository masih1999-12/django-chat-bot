# Generated by Django 4.2.14 on 2024-08-07 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custompermision',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]