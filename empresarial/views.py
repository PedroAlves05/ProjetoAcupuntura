from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth import authenticate, login
from datetime import datetime, timedelta, time
from django.db.models.functions import Concat
from django.db.models import Value
from django.contrib.admin.views.decorators import staff_member_required
from agendamentos.models import AgendarExame, Horario
from .models import Procedimentos, Gastos

# Create your views here.
@staff_member_required 
def filtrar(request):
    clientes = User.objects.filter(is_staff=False)

    nome_completo = request.GET.get('nome')
    email = request.GET.get('email')
    username = request.GET.get('username')

    if email:
        clientes = clientes.filter(email__contains = email)
    if nome_completo:
        clientes = clientes.annotate(
            full_name=Concat('first_name', Value(' '), 'last_name')
        ).filter(full_name__contains=nome_completo)
    if username:
        clientes = clientes.filter(username__contains = username)


    return render(request, 'filtrar.html', {'clientes': clientes})

@staff_member_required 
def cliente(request, cliente_id):
    cliente = User.objects.get(id=cliente_id)
    exames = AgendarExame.objects.filter(usuario=cliente)
    return render(request, 'cliente.html', {'cliente': cliente, 'exames': exames})

@staff_member_required 
def exame_cliente(request, exame_id):
    exame = AgendarExame.objects.get(id=exame_id)
    if Procedimentos.objects.filter(procedimento=exame).exists():
        procedimento1 = Procedimentos.objects.get(procedimento=exame)
        return render(request, 'exame_cliente.html', {'exame': exame, "procedimentos":procedimento1})
    return render(request, 'exame_cliente.html', {'exame': exame})

@staff_member_required 
def criar_procedimento(request, exame_id):
    exame = AgendarExame.objects.get(id=exame_id)
    Olho = request.POST.get("Olho")  == "on"
    Olfativo = request.POST.get("Olfativo")  == "on"
    Mandibular = request.POST.get("Mandibular")  == "on"
    Pulmões = request.POST.get("Pulmões")  == "on"
    Auditivo = request.POST.get("Auditivo")  == "on"
    Estômago = request.POST.get("Estômago")  == "on"
    Garganta = request.POST.get("Garganta")  == "on"
    Gônadas = request.POST.get("Gônadas")  == "on"
    Pâncreas = request.POST.get("Pâncreas")  == "on"
    Coração = request.POST.get("Coração")  == "on"
    Fígado = request.POST.get("Fígado")  == "on"
    Retal = request.POST.get("Retal")  == "on"
    Ciático = request.POST.get("Ciático")  == "on"
    Joelho = request.POST.get("Joelho")  == "on"
    Rim = request.POST.get("Rim")  == "on"
    Trigêmeo = request.POST.get("Trigêmeo")  == "on"
    Agressividade = request.POST.get("Agressividade")  == "on"
    Tragus = request.POST.get("Tragus")  == "on"
    Pele = request.POST.get("Pele")  == "on"
    Ombro = request.POST.get("Ombro")  == "on"
    Zero = request.POST.get("Zero")  == "on"
    M_inferiores = request.POST.get("M_inferiores")  == "on"
    M_superiores = request.POST.get("M_superiores")  == "on"
    Alergia = request.POST.get("Alergia")  == "on"
    Darwin = request.POST.get("Darwin")  == "on"
    Síntese = request.POST.get("Síntese")  == "on"
    Tálamo = request.POST.get("Tálamo")  == "on"
    Occipital = request.POST.get("Occipital")  == "on"
    Genital = request.POST.get("Genital")  == "on"
    Medular = request.POST.get("Medular")  == "on"


    Hipotálamo = request.POST.get("Hipotálamo")  == "on"
    Sacro = request.POST.get("Sacro")  == "on"
    Ponto_de_muro = request.POST.get("Ponto_de_muro")  == "on"
    Cóccix = request.POST.get("Cóccix")  == "on"
    Cervical = request.POST.get("Cervical")  == "on"
    Hipófise = request.POST.get("Hipófise")  == "on"
    Torácica = request.POST.get("Torácica")  == "on"
    Pineal = request.POST.get("Pineal")  == "on"
    Lombar = request.POST.get("Lombar")  == "on"
    adrenal = request.POST.get("adrenal")  == "on"

    relatorio = request.POST.get("Relatorio")

    pagamento = request.POST.get("Confirmar_pagamento")  == "on"
    if Procedimentos.objects.filter(procedimento=exame).exists():
        procedimento1 = Procedimentos.objects.get(procedimento=exame)
        procedimento1.pontosUsados=relatorio
        procedimento1.Olho=Olho
        procedimento1.Olfativo=Olfativo
        procedimento1.Mandibular=Mandibular
        procedimento1.Pulmões=Pulmões
        procedimento1.Auditivo=Auditivo
        procedimento1.Estômago=Estômago
        procedimento1.Garganta=Garganta
        procedimento1.Gônadas=Gônadas
        procedimento1.Pâncreas=Pâncreas
        procedimento1.Coração=Coração
        procedimento1.Fígado=Fígado
        procedimento1.Retal=Retal
        procedimento1.Ciático=Ciático
        procedimento1.Joelho=Joelho
        procedimento1.Rim=Rim
        procedimento1.Trigêmeo=Trigêmeo
        procedimento1.Agressividade=Agressividade
        procedimento1.Tragus=Tragus
        procedimento1.Pele=Pele
        procedimento1.Ombro=Ombro
        procedimento1.Zero=Zero
        procedimento1.M_inferiores=M_inferiores
        procedimento1.M_superiores=M_superiores
        procedimento1.Alergia=Alergia
        procedimento1.Darwin=Darwin
        procedimento1.Síntese=Síntese
        procedimento1.Tálamo=Tálamo
        procedimento1.Occipital=Occipital
        procedimento1.Genital=Genital
        procedimento1.Medular=Medular
        procedimento1.Hipotálamo=Hipotálamo
        procedimento1.Sacro=Sacro
        procedimento1.Ponto_de_muro=Ponto_de_muro
        procedimento1.Cóccix=Cóccix
        procedimento1.Cervical=Cervical
        procedimento1.Hipófise=Hipófise
        procedimento1.Torácica=Torácica
        procedimento1.Pineal=Pineal
        procedimento1.Lombar=Lombar
        procedimento1.adrenal=adrenal
        procedimento1.Pagamento=pagamento
    
        procedimento1.save()
    else:
        procedimento2 = Procedimentos(
            procedimento=exame,
            pontosUsados=relatorio,
            Olho=Olho,
            Olfativo=Olfativo,
            Mandibular=Mandibular,
            Pulmões=Pulmões,
            Auditivo=Auditivo,
            Estômago=Estômago,
            Garganta=Garganta,
            Gônadas=Gônadas,
            Pâncreas=Pâncreas,
            Coração=Coração,
            Fígado=Fígado,
            Retal=Retal,
            Ciático=Ciático,
            Joelho=Joelho,
            Rim=Rim,
            Trigêmeo=Trigêmeo,
            Agressividade=Agressividade,
            Tragus=Tragus,
            Pele=Pele,
            Ombro=Ombro,
            Zero=Zero,
            M_inferiores=M_inferiores,
            M_superiores=M_superiores,
            Alergia=Alergia,
            Darwin=Darwin,
            Síntese=Síntese,
            Tálamo=Tálamo,
            Occipital=Occipital,
            Genital=Genital,
            Medular=Medular,
            Hipotálamo=Hipotálamo,
            Sacro=Sacro,
            Ponto_de_muro=Ponto_de_muro,
            Cóccix=Cóccix,
            Cervical=Cervical,
            Hipófise=Hipófise,
            Torácica=Torácica,
            Pineal=Pineal,
            Lombar=Lombar,
            adrenal=adrenal,
            Pagamento=pagamento,
        )
        procedimento2.save()
    return redirect(f'/empresarial/exame_cliente/{exame_id}')

@staff_member_required 
def ver_agendamentos(request):
    agendamentos = AgendarExame.objects.filter(cancelado=False)
    data = request.GET.get('data')
    
    if data:
        # Assumindo que 'data' é o campo de relacionamento entre 'AgendarExame' e 'Horario'
        agendamentos = agendamentos.filter(data__data=data)
            
    # ... restante do seu código, se houver ...
    # Pode ser que você queira renderizar um template com os agendamentos, por exemplo.


        
    return render(request, 'ver_agendamentos.html', {'agendamentos':agendamentos})


@staff_member_required
def ver_financeiro(request):
    total_ganho = 0
    total_gasto = 0
    for procedimento in Procedimentos.objects.filter(Pagamento=True):
        ganho = procedimento.procedimento.exame.preco
        total_ganho += ganho
    for gasto in Gastos.objects.filter():
        despesa = gasto.valorGasto
        total_gasto += despesa
    saldo = total_ganho - total_gasto
    despesas = Gastos.objects.filter()
    receitas = Procedimentos.objects.filter(Pagamento = True)
    return render(request, 'ver_financeiro.html', {'saldo':saldo, 'despesas': despesas, 'receitas': receitas})