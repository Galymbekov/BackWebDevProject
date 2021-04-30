from django.shortcuts import render
from django.http.response import JsonResponse
from shop.models import *
from rest_framework.views import APIView
from shop.serializers import *
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated


class ProductList(APIView):
    def get(self, request):
        products = Shop.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductLAPIView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ProductSerializer
    permission_classes = IsAuthenticated
