from django.urls import path, include
from registration.views import *
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('register/', RegUser)
]