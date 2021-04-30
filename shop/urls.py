from django.contrib import admin
from django.urls import path, include
from shop.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('register/', include('registration.urls')),
    path('shop/', ProductList.as_view())
]
