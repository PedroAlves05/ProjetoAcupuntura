from django.urls import path
from . import views

urlpatterns = [
    path('filtrar/', views.filtrar, name='filtrar'),
    path('cliente/<int:cliente_id>', views.cliente, name="cliente"),
    path('exame_cliente/<int:exame_id>', views.exame_cliente, name="exame_cliente"),
    path('ver_agendamentos', views.ver_agendamentos, name="ver_agendamentos"),
    path('criar_procedimento/<int:exame_id>', views.criar_procedimento, name="criar_procedimento"),
    path('ver_financeiro', views.ver_financeiro, name="ver_financeiro"),
]