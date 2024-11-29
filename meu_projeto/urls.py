# app_cad_usuarios/urls.py
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    path('', views.login, name='login'),  # Página de login
    path('opcoes/', views.opcoes, name='opcoes'),  # Página de opções
    path('cadastro/', views.cadastro, name='cadastro'),  # Cadastro de novos alunos
    path('editar/', views.editar, name='editar'),  # Edição de alunos cadastrados
    
]