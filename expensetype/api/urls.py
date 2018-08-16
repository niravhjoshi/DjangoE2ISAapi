from django.contrib import admin
from django.conf.urls import url, include
from .views import  ExpenseTypeAPIView,ExpenseTypeDetailAPIView

urlpatterns = [
    url(r'^$',ExpenseTypeAPIView.as_view()),
    url(r'^(?P<ExpenseType_id>\d+)/$',ExpenseTypeDetailAPIView.as_view()),

]
