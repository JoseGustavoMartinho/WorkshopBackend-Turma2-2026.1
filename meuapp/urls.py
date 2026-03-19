from django.urls import path
from .views import listar_pessoas, criar_pessoas, atualizar_pessoa, deletar_pessoa

urlpatterns = [
    path('listar/', listar_pessoas, name='listar_pessoas'),
    path('criar/', criar_pessoas, name='criar_pessoas'),
    path('editar/<int:pk>/', atualizar_pessoa, name= 'atualizar_pessoa'),
    path('deletar/<int:pk>/', deletar_pessoa, name= 'deletar_pessoa'),
]