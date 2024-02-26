from django.shortcuts import render, redirect

from django.contrib.auth.models import User

def register(request):

    c = {}

    if request.method == 'POST':

        username = request.POST.get('u').lower()
        password = request.POST.get('p')

        user = User(username = username)
        user.set_password(password)
        user.save()

        return redirect('/')

    return render(request, 'auth/register.html', c)