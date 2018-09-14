from django.contrib import admin
from django.conf.urls import url, include
from .views import  ExpenseEntryDetailAPIView,ExpenseEntryAPIView

urlpatterns = [
    url(r'^$',ExpenseEntryAPIView.as_view()),
    url(r'^(?P<ExpensesID>\d+)/$',ExpenseEntryDetailAPIView.as_view()),
   ]
