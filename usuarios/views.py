from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth import authenticate, login
from datetime import datetime

# Create your views here.

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        username = request.POST.get('username')
        
        if not confirmar_senha == senha:
            messages.add_message(request, constants.ERROR, 'As senhas não se coincidem!')
            return redirect('/usuarios/cadastro')
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha deve conter no minimo 7 caracteres!')
            return redirect('/usuarios/cadastro')
        
        
        user = User.objects.create_user(
            first_name = primeiro_nome,
            last_name = ultimo_nome,
            username = username,
            email = email,
            password = senha,   
        )
        messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso! Por favor faça seu login.')

        return redirect('/usuarios/Login')




def Login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username_digitado = request.POST.get('username')
        senha_digitada = request.POST.get('senha')
        
        user = authenticate(username=username_digitado, password=senha_digitada)

        if user:
            login(request, user)
            messages.add_message(request, constants.SUCCESS, 'Você fez login com sucesso!')
            return redirect('/agendamentos/realizar_agendamento')
        
        else:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha inválidos!')
            return redirect('/usuarios/Login')