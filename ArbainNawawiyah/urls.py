from django.urls import path
from . import views

urlpatterns = [
    path('ArbainNawawiyah/', views.ArbainNawawiyah, name='ArbainNawawiyah'),
]