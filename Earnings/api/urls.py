from django.contrib import admin
from django.conf.urls import url, include
from .views import  EarningEntryAPIView,EarningEntryDetailAPIView

urlpatterns = [
    url(r'^$',EarningEntryAPIView.as_view()),
    url(r'^(?P<Id>\d+)/$',EarningEntryDetailAPIView.as_view()),
   ]
