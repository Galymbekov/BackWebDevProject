from login.models import *
from login.serializers import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse


class LoginUser(APIView):
    def get(self, request):
        serializer =LoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def user_detail(request, user_id):

    try:
        user = Login.objects.get(id=user_id)
    except Login.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = LoginSerializer(user)
        return Response(serializer.data)