from django.urls import path
from . import views

urlpatterns = [
    path('draw/', views.home, name = 'Home Page')
]