from django.shortcuts import render, HttpResponse
from core.models import Evento

# Create your views here.
# def index(request):
#     return redirect('/agenda/')

def eventos(request, nome_evento):
    event = Evento.objects.get(titulo=nome_evento)
    local = event.local
    return HttpResponse('Seu evento será em {}.'.format(local))

def listaeventos(request):
    evento = Evento.objects.all()
    response = {'eventos':evento}
    return render(request, 'Agenda.html', response)
