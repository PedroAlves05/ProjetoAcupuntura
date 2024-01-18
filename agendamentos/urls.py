from django.urls import path
from . import views

urlpatterns = [
    path('realizar_agendamento/', views.realizar_agendamento, name='realizar_agendamento'),
    path('mostrar_horarios_disponiveis/', views.mostrar_horarios_disponiveis, name='mostrar_horarios_disponiveis'), 
    path('gerenciar_agendamentos/', views.gerenciar_agendamentos, name='gerenciar_agendamentos'), 
    path('fechar_pedido/', views.fechar_pedido, name="fechar_pedido"),
    path("cancelar_agendamento/<int:pedido_id>", views.cancelar_agendamento, name="cancelar_agendamento"),
]
