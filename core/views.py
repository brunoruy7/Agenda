from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
# def index(request):
#     return redirect('/agenda/')

def login_user(request):
    return render(request, 'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido.")
    return redirect('/')

@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/')

def even(request, nome_evento):
    event = Evento.objects.get(titulo=nome_evento)
    local = event.local
    return HttpResponse('Seu evento será em {}.'.format(local))

@login_required(login_url='/login/')
def listaeventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    response = {'eventos':evento}
    return render(request, 'Agenda.html', response)

@login_required(login_url='/login/')
def evento(request):
    return render(request, 'evento.html')

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        local = request.POST.get('local')
        descricao = request.POST.get('descricao')
        user = request.user

        evento = Evento.objects.create(titulo=titulo,
                                       data_evento=data_evento,
                                       local=local,
                                       descricao=descricao,
                                       usuario=user)
    return redirect("/")
