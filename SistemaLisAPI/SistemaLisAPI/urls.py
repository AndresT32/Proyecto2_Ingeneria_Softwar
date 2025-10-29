from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/laboratoristas/', include('APILaboratoristas.urls')),
    path('api/login/', include('APILogin.urls')),
    path('api/resultados/', include('APIResultados.urls')),
    path('api/pacientes/', include('APIPaciente.urls')),
]
