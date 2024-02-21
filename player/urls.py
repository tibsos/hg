from django.urls import path

from .views import *

app_label = 'player'

urlpatterns = [

    path('register', register, name = 'register'),

]