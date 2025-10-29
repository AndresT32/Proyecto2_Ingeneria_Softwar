from django.urls import path
from .views import PacientesView

urlpatterns = [
    path('pacientes/', PacientesView.as_view(), name='pacientes_list'),
    path('pacientes/<str:cod_ingreso>/', PacientesView.as_view(), name='paciente_detail'),
]
