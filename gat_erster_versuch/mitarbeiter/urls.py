from django.urls import path
from . import views



urlpatterns = [
    path('erstelle_mitarbeiter/', views.erstelle_mitarbeiter, name='erstelle_mitarbeiter_'),
    path('alle_mitarbeiter/', views.mitarbeiter, name='alle_mitarbeiter_' )

]