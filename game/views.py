from django.shortcuts import render

def game(request):

    c = {}

    c['user'] = request.user

    if request.user.is_authenticated:

        c['player'] = request.user.player

    return render(request, 'game.html', c)