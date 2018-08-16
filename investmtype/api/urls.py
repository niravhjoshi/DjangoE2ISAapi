from django.contrib import admin
from django.conf.urls import url, include
from .views import InvTypeAPIView,InvTypeDetailAPIView

urlpatterns = [
    url(r'^$',InvTypeAPIView.as_view()),
    url(r'^(?P<Invtype_id>\d+)/$',InvTypeDetailAPIView.as_view()),

]
