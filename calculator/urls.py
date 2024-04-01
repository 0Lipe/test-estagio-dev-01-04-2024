from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
  path('', views.view1, name='view1'),
  path("calculate", views.view2, name='calculate')  # Corrigido para "calculate"
]
