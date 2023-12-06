from django.urls import path
from django.http import HttpResponse
from . import views



urlpatterns = [
    path('aufgabenzettel/', views.create_aufgabenzettel, name='aufgabenzettel_'),
]