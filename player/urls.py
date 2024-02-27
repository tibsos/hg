from django.urls import path

from .views import *

app_label = 'player'

urlpatterns = [

    path('login', log_in, name = 'login'),
    path('register', register, name = 'register'),
    path('logout', log_out, name = 'logout'),

    path('check-username', check_username, name = 'check-username'),

    path('cb', change_background),

]