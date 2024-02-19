from django.shortcuts import render

def game(request):

    c = {}

    return render(request, 'game.html', c)