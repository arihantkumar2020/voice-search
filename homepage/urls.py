from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('speaktosearch', views.speech, name = 'speechToText'),
    path('texttosearch', views.text, name = 'texttoweb'),
]