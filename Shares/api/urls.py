from django.contrib import admin
from django.conf.urls import url, include
from .views import  SharesEntryAPIView,SharesEntryDetailAPIView

urlpatterns = [
    url(r'^$',SharesEntryAPIView.as_view()),
    url(r'^(?P<SharesID>\d+)/$',SharesEntryDetailAPIView.as_view()),
   ]
