from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth import authenticate, login
from datetime import datetime, timedelta, time
from .models import Horario, Exames, AgendarExame
from django.db.models.functions import Concat
from django.db.models import Value
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.utils import timezone


# Create your views here.
@login_required
def realizar_agendamento(request):
    tipos_exames = Exames.objects.all()
    
    if request.method == "GET":
        return render(request, 'realizar_agendamento.html', {'exames': tipos_exames})
    elif request.method == "POST":
        hora_selecionada = request.POST.get('hora')
        exames_id = request.POST.getlist('exames')
        data_selecionada = request.POST.get('data')  # Obtendo a data do formulário
        #horarios_disponiveis = Horario.objects.filter(data=data_selecionada, disponivel=True)
        solicitacao_exames = Exames.objects.filter(id__in=exames_id)
        preco_total = 0
        for i in solicitacao_exames:
            if i.disponivel:
                preco_total += i.preco
        return render(request, 'realizar_agendamento.html', {'hora': hora_selecionada, 'exames': tipos_exames, 'solicitacao_exames': solicitacao_exames, 'preco_total': preco_total, 'data': data_selecionada})





@login_required
def mostrar_horarios_disponiveis(request):
    if request.method == "GET":
        return render(request, 'mostrar_horarios_disponiveis.html')
    elif request.method == "POST":
        exame_id = request.POST.get('exame')
        exame_selecionado = get_object_or_404(Exames, id=exame_id)
        data_selecionada = request.POST.get('data')
        horarios_disponiveis = Horario.objects.filter(data=data_selecionada, disponivel=True)
        horarios_disponiveis_novo = []

        
        for horario in horarios_disponiveis:
            horario_agendamento_timedelta = timedelta(hours=horario.hora.hour, minutes=horario.hora.minute)
            horario_final_timedelta = timedelta(hours=exame_selecionado.duracao.hour, minutes=exame_selecionado.duracao.minute)
            horario_final_timedelta += horario_agendamento_timedelta  # Adiciona o tempo do exame ao horário original

            # Verifica disponibilidade para intervalos de 15 minutos
            intervalo = timedelta(minutes=15)
            horario_atual_timedelta = horario_agendamento_timedelta

            while horario_atual_timedelta <= horario_final_timedelta:
                horario_atual_datetime = datetime.combine(datetime.strptime(data_selecionada, '%Y-%m-%d'), time()) + horario_atual_timedelta
                horario_atual = horario_atual_datetime.time()

                # Verificar se o horário atual está disponível e se é no futuro
                if datetime.combine(datetime.strptime(data_selecionada, '%Y-%m-%d'), horario_atual) > datetime.now():
                    horario_atual_disponivel = Horario.objects.filter(data=data_selecionada, hora=horario_atual, disponivel=True).exists()

                    if not horario_atual_disponivel:
                        break  # Sai do loop se encontrar um horário indisponível
                else:
                    break  # Sai do loop se encontrar um horário antes do tempo da requisição

                horario_atual_timedelta += intervalo  # Avança para o próximo intervalo

            else:
                # Se o loop não foi interrompido, todos os intervalos estão disponíveis e a data e hora são posteriores à requisição
                horarios_disponiveis_novo.append(horario)
        
        return render(request, 'mostrar_horarios_disponiveis.html', {'horarios': horarios_disponiveis_novo, 'data': data_selecionada, 'exame': exame_selecionado})



@login_required
def fechar_pedido(request):
    if request.method == "GET":
        return render(request, 'gerenciar_agendamentos.html')
    elif request.method == "POST":
        data_selecionada = request.POST.get("data")
        hora_selecionada = request.POST.get("hora")
        exame_selecionado_id = request.POST.get("exame")
        exame_selecionado = get_object_or_404(Exames, id=exame_selecionado_id)
        horario_selecionado = get_object_or_404(Horario, data=data_selecionada,hora=hora_selecionada)
        solicitar_exame = AgendarExame(
            usuario=request.user,
            exame=exame_selecionado,
            data=horario_selecionado
        )
        solicitar_exame.save()
        
        horario_agendamento_timedelta = timedelta(hours=horario_selecionado.hora.hour, minutes=horario_selecionado.hora.minute)

        # Converta a duração do exame para um objeto timedelta
        duracao_do_exame_timedelta = timedelta(hours=exame_selecionado.duracao.hour, minutes=exame_selecionado.duracao.minute)

        # Calcule o horário final do exame adicionando a duração do exame ao horário de agendamento
        horario_final_do_exame_timedelta = horario_agendamento_timedelta + duracao_do_exame_timedelta

        # Itere sobre os horários entre o horário de agendamento e o horário final do exame
        horario_atual_timedelta = horario_agendamento_timedelta
        
        while horario_atual_timedelta <= horario_final_do_exame_timedelta:
            # Converta o horário de timedelta de volta para um objeto time
            horas, minutos = divmod(horario_atual_timedelta.seconds // 60, 60)
            horario_atual = time(hour=horas, minute=minutos)

            # Consulte o objeto Horario com o horario_atual
            try:
                cancelar_horario = Horario.objects.get(data=data_selecionada,hora=horario_atual)
                cancelar_horario.disponivel = False
                cancelar_horario.save()
            except Horario.DoesNotExist:
                # Lide com o caso em que o objeto Horario com esse horário não existe
                pass

            # Incremente o horario_atual_timedelta por um intervalo de 30 minutos (ou o intervalo desejado)
            horario_atual_timedelta += timedelta(minutes=15) 
        
        messages.add_message(request, constants.SUCCESS, 'Pedido de exame concluído com sucesso')
        return redirect('/agendamentos/gerenciar_agendamentos/')
        
@login_required
def gerenciar_agendamentos(request):
    usuario = request.user
    agora = timezone.now()

    # Filtrar agendamentos futuros para o usuário atual que não foram cancelados
    pedidos_exames = AgendarExame.objects.filter(usuario=usuario, data__data__gte=agora, cancelado=False).order_by('data__data', 'data__hora')
    return render(request, 'gerenciar_agendamentos.html', {'pedidos_exames': pedidos_exames})

@login_required
def cancelar_agendamento(request, pedido_id):
    pedido = AgendarExame.objects.get(id=pedido_id)

    if not pedido.usuario == request.user:
        messages.add_message(request, constants.ERROR, 'Esse pedido não é seu')
        return redirect('/agendamentos/gerenciar_agendamentos/')
    
    pedido.cancelado = True
    pedido.save()
    
    horario_selecionado = pedido.data.hora
    data_selecionada = pedido.data.data
    horario_agendamento_timedelta = timedelta(hours=horario_selecionado.hour, minutes=horario_selecionado.minute)
    exame_selecionado = pedido.exame.duracao
    # Converta a duração do exame para um objeto timedelta
    duracao_do_exame_timedelta = timedelta(hours=exame_selecionado.hour, minutes=exame_selecionado.minute)

    # Calcule o horário final do exame adicionando a duração do exame ao horário de agendamento
    horario_final_do_exame_timedelta = horario_agendamento_timedelta + duracao_do_exame_timedelta

    # Itere sobre os horários entre o horário de agendamento e o horário final do exame
    horario_atual_timedelta = horario_agendamento_timedelta
    
    while horario_atual_timedelta <= horario_final_do_exame_timedelta:
        # Converta o horário de timedelta de volta para um objeto time
        horas, minutos = divmod(horario_atual_timedelta.seconds // 60, 60)
        horario_atual = time(hour=horas, minute=minutos)

        # Consulte o objeto Horario com o horario_atual
        try:
            cancelar_horario = Horario.objects.get(data=data_selecionada,hora=horario_atual)
            cancelar_horario.disponivel = True
            cancelar_horario.save()
        except Horario.DoesNotExist:
            # Lide com o caso em que o objeto Horario com esse horário não existe
            pass

        # Incremente o horario_atual_timedelta por um intervalo de 30 minutos (ou o intervalo desejado)
        horario_atual_timedelta += timedelta(minutes=15) 
    messages.add_message(request, constants.SUCCESS, 'Pedido cancelado com sucesso')
    return redirect('/agendamentos/gerenciar_agendamentos/')