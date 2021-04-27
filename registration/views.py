from registration.models import *
from registration.serializers import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse


class RegUser(APIView):
    def post(self, request):
        serializer =RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def reg_detail(request, user_id):

    try:
        user = Registration.objects.get(id=user_id)
    except Registration.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'PUT':
        serializer = RegistrationSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})