from django.urls import path

from .views import *

urlpatterns = [

    path('', game, name = 'game'),

    path('change-background', change_background, name = 'change-background'),

]