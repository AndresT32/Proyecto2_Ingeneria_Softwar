from django.urls import path
from .views import LoginView

urlpatterns = [
    path('users/', LoginView.as_view()),       # GET all / POST
    path('users/<int:id>/', LoginView.as_view())  # GET, PUT, DELETE por id
]

