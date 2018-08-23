"""DjangoE2ISAapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
from .restconf import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('persons.api.urls'),name='home'),
    #url(r'^api/persons/',include('persons.api.urls'),name='HOME'),
    url(r'^api/eartypes/',include('earningtype.api.urls')),
    url(r'^api/exptypes/',include('expensetype.api.urls')),
    url(r'^api/invtypes/',include('investmtype.api.urls')),
    url(r'^api/auth/jwt/',obtain_jwt_token),
    url(r'^api/auth/jwt/refresh',refresh_jwt_token),
    url(r'^api/auth/jwt/verify',verify_jwt_token),
    url(r'^new',views.index),
    url(r'^oauth/', include('social_django.urls', namespace='social'))
]