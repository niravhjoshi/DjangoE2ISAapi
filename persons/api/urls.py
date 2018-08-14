from django.contrib import admin
from django.conf.urls import url, include
from .views import PersonListSearchAPIView
urlpatterns = [
    url(r'^$',PersonListSearchAPIView.as_view()),
  # url(r'^(?P<id>.*)/$',PersonDetailAPIView.as_view()),
  # url(r'^(?P<id>.*)/update/$',PersonUpdateAPIView.as_view()),
  # url(r'^(?P<id>.*)/delete/$',PersonDeleteAPIView.as_view()),
]
#Start with
# /api/persons/ --> List view
# /api/persons/create -->create person
# /api/persons/12 ---> Detail view
# /api/persons/12 ---> Update view
# /api/persons/12 ---> Dlete view

#End with
# /api/persons/--> List -> CRUD
# /api/persons/12 --> Details -> CRUD

#Final with
# /api/persons/  -> CRUD and LS
