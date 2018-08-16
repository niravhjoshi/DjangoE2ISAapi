from django.contrib import admin
from django.conf.urls import url, include
from .views import  EarningTypeAPIView,EarningTypeDetailAPIView

urlpatterns = [
    url(r'^$',EarningTypeAPIView.as_view()),
    url(r'^(?P<EarnType_id>\d+)/$',EarningTypeDetailAPIView.as_view()),

]
