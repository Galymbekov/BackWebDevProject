from django.urls import path, include
from login.views import *
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('start/', ObtainAuthToken.as_view(), LoginUser),
    path('logout/', LogOut.as_view())
]