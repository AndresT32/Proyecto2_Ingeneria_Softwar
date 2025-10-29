from django.urls import path
from .views import ResultadosView

urlpatterns = [
    path('resultados/', ResultadosView.as_view()),                # GET all / POST
    path('resultados/<int:id_resultado>/', ResultadosView.as_view())  # GET, PUT, DELETE
]

