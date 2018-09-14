from django.contrib import admin
from django.conf.urls import url, include
from .views import  EarningEntryDetailAPIView,EarningEntryAPIView

urlpatterns = [
    url(r'^$',EarningEntryAPIView.as_view()),
    url(r'^(?P<EarningsId>\d+)/$',EarningEntryDetailAPIView.as_view()),
   ]
