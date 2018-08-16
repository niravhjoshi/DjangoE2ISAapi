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
from persons.views import PersonSerializDetailView,PersonSerializeListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/persons/',include('persons.api.urls')),
    url(r'^api/eartypes/',include('earningtype.api.urls')),
    url(r'^api/exptypes/',include('expensetype.api.urls')),
    url(r'^api/invtypes/',include('investmtype.api.urls')),

#    url(r'^person/$', person_detail_view,),
#    url(r'^person/cbv/$', JsonCBV.as_view(),),
    #url(r'^person/PersonSerializDetailView/(?P<puser_id>\d+)/$', PersonSerializDetailView.as_view(),),
    #url(r'^person/PersonSerializListView/$', PersonSerializeListView.as_view(),),
#    url(r'^person/cbv2/$', JsonCBV2.as_view(),),
]