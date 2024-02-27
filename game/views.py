from django.shortcuts import render

def game(request):

    c = {}

    c['user'] = request.user

    if request.user.is_authenticated:

        player = request.user.player

        c['player'] = player

    return render(request, 'game.html', c)