from rest_framework import serializers
from registration.models import *
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    confpass = serializers.CharField(required=True)

    def create(self, validated_data):
        user = Registration.objects.create(name=validated_data.get('username'),
                                           email=validated_data.get('email'),
                                           username=validated_data.get('username'),
                                           password=validated_data.get('password'),
                                           confpass=validated_data.get('confpass'))
        return user


class RegSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'username', 'password', 'confpass']

    def create(self, validated_data):
        user = User(
            name=validated_data['name'],
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.set_password(validated_data['confpass'])
        user.save()
        return user


