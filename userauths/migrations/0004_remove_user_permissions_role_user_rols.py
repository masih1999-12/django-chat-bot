# Generated by Django 4.2.14 on 2024-08-08 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0003_alter_custompermision_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='permissions',
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('permisions', models.ManyToManyField(to='userauths.custompermision')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='rols',
            field=models.ManyToManyField(to='userauths.role'),
        ),
    ]
