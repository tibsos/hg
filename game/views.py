from django.shortcuts import render

from django.http import HttpResponse

from .models import *

def change_background(request):

    if request.method == 'POST':

        background = request.POST.get('b')

        request.session['background'] = background

        return HttpResponse('K')

def change_skin(request):

    if request.method == 'POST':

        skin = request.POST.get('s')

        request.session['skin'] = skin

        return HttpResponse('K')

def game(request):

    c = {}

    skin = request.session.get('skin')

    if skin is None:

        c['skin'] = 'alien'
    
    else: c['skin'] = skin

    c['background'] = request.session.get('background')

    e = Event.objects.get(name = 'Игра')
    e.count += 1
    e.save()

    return render(request, 'game.html', c)

def game_count(request):

    e = Event.objects.get(name = 'play')
    e.count += 1
    e.save()

    return HttpResponse('K')