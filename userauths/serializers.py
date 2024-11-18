from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import transaction
from .models import User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token= super().get_token(user)

        token['full_name'] = user.full_name
        token['email'] = user.email
        token['username'] = user.username

        try:
            token['vendor_id'] = user.vendor.id
        except AttributeError:
            token['vendor_id'] = 0

        return token
    

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['full_name', 'email', 'phone', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password does not match"})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        email = validated_data.get('email', '')

        if '@' not in email:
            raise ValidationError("Invalid email format")

        user = User.objects.create(
            full_name=validated_data['full_name'],
            email=email,
            phone=validated_data['phone'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

class ProfileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('full_name', 'phone')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','phone','first_name','last_name','date_joined',
                    'rols')
        read_only_fields = ('id','date_joined')
    def get_fields(self):
        fields=super().get_fields()
        if self.context.get('request') and self.context['request'].method in ('POST','PUT','PATCH'):
            fields['rols']=serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(),many=True)
            if self.context['request'].method == 'POST':
                fields['password']=serializers.CharField(max_length=128)
        return fields
    
    @transaction.atomic
    def create(self, validated_data):
        password=validated_data.pop('password',None)
        obj:User = super().create(validated_data)
        obj.set_password(password)
        return obj
    
    @transaction.atomic
    def update(self, instance, validated_data):
        password=validated_data.pop('password',None)
        obj:User= super().update(instance, validated_data)
        if password:
            obj.set_password(password)
        return obj
