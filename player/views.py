from django.shortcuts import render

def register(request):

    c = {}

    return render(request, 'auth/register.html', c)