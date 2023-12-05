from django.urls import path
from . import views

urlpatterns = [
    path('mitarbeiter/', views.mitarbeiter, name='mitarbeiter_'),
]