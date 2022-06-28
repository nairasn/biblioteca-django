import logging
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('plataforma/', views.plataforma, name = 'plataforma'),
    path('biblioteca/', views.biblioteca, name = 'biblioteca'),
    path('livros_cadastro/', views.livros_cadastro, name = 'livros_cadastro'),
        
]