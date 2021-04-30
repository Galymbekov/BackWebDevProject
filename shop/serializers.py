from rest_framework import serializers
from shop.models import *
from django.contrib.auth.models import User


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    like = serializers.BooleanField(default=False)
    price = serializers.FloatField(default=None)
    description = serializers.CharField(default=None)

    def create(self, validated_data):
        return Shop(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.like = validated_data.get('like', instance.like)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
