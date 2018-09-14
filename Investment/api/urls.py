from django.contrib import admin
from django.conf.urls import url, include
from .views import  InvestmentEntryAPIView,InvestmentEntryDetailAPIView

urlpatterns = [
    url(r'^$',InvestmentEntryAPIView.as_view()),
    url(r'^(?P<InvestmentId>\d+)/$',InvestmentEntryDetailAPIView.as_view()),
   ]
