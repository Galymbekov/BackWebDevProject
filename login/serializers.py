from rest_framework import serializers
from login.models import *
from django.contrib.auth.models import User

class LoginSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    remember = serializers.BooleanField(default=False)

    def read(self, validated_data):
        user = Login.objects.create(username=validated_data.get('username'),
                                    password=validated_data.get('password'),
                                    remember=validated_data.get('remember'))
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'remember']

    def read(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user