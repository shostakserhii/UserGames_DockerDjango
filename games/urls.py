from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('add_user/', add_user, name='add_user'),
    path('user_games', user_games, name='user_games' ),
    path('delete_user', delete_user, name='delete_user')
]