from django.shortcuts import render

from django.http import HttpResponse

def change_background(request):

    if request.method == 'POST':

        background = request.POST.get('b')

        request.session['background'] = background

        return HttpResponse('K')

def game(request):

    c = {}

    c['skin'] = request.session.get('skin')
    c['background'] = request.session.get('background')


    return render(request, 'game.html', c)