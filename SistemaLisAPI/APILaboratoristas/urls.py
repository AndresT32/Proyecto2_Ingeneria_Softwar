from django.urls import path
from .views import LaboratoristasView  # cambia según la app

urlpatterns = [
    path('laboratoristas/', LaboratoristasView.as_view()),
    path('laboratoristas/<str:cod_laboratorista>/', LaboratoristasView.as_view()),
]
