from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

def register(request):

    c = {}

    if request.method == 'POST':

        username = request.POST.get('u').lower()
        password = request.POST.get('p')
        email = request.POST.get('e')

        user = User(username = username)
        user.set_password(password)
        user.email = email
        user.save()

        user = authenticate(username = username, password = password)
        login(request, user)

        return redirect('/')

    return render(request, 'auth/register.html', c)

def log_in(request):

    c = {}

    if request.method == 'POST':

        u = authenticate(

            username = request.POST.get('u'),
            password = request.POST.get('p'),

        )

        if u:

            login(request, u)
            return redirect('/home/')

        else: 

            return render(request, 'auth/login.html', {'e': True})
    
    return render(request, 'auth/login.html', c)

def log_out(request):

    logout(request)

    return redirect('/')

def check_username(request):

    u = request.POST.get('u')

    if User.objects.filter(username = u).exists():

        return JsonResponse({'u': 'n'})

    else:

        return JsonResponse({'u': 'y'})
    
def change_background(request):

    background = request.POST.get('b')

    player = request.user.player

    player.background = background
    
    player.save()

    return HttpResponse('K')