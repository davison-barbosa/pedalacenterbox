from django.urls import path
from . import views


urlpatterns = [
    path('', views.cadastro_list, name='cadastro_list'),
    path('home/', views.cadastro_list, name='cadastro_list'),
    path('cadastro/novo/', views.cadastro_novo, name='cadastro_novo'),
    path('cadastro', views.cadastro_novo, name='cadastro_novo'),
    path('lista/pessoas/', views.cadastro_list_pessoas, name='cadastro_list_pessoas'),
    path('inscricao/confirmacao/', views.confirmacao_inscricao, name='confirmacao_inscricao'),
    
]