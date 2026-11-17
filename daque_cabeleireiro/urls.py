from django.urls import path
from core_app.views import reservar_horario

urlpatterns = [
    path('reservar/', reservar_horario),
]