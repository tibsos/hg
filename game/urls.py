from django.urls import path

from .views import *

urlpatterns = [

    path('', game, name = 'game'),

    path('change-background', change_background, name = 'change-background'),
    path('change-skin', change_skin, name = 'change-skin'),

    path('game-count', game_count, name = 'game-count'),

]