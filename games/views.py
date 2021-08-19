import time

from django.shortcuts import render

from games.src.client import Client
from games.src.user_db import Users


MENU = ["Check all users' games", "See user's games", "Delete user from database"]
        

def index(request):
    return render(request, 'games/index.html', {'menu': MENU, 'title': 'Games'})

def add_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        passwd = request.POST.get('password')
        user_manager = Users()
        result = user_manager.add_users(name, surname, email, passwd)
        return render(request, 'games/add_user.html', {'top': result})
    return render(request, 'games/add_user.html', {'top': 'Fill out the fields'})

def user_games(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user_manager = Client()
        games = user_manager.user_games(email)
        return render(request, 'games/games.html', {'games': games, 'title': 'Games'})
    return render(request, 'games/delete_user.html', {'title':"User's games", 'head':'Check user\'s games by email'})

def delete_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user_manager = Client()
        user_manager.remove_user(email)
        return render(request, 'games/games.html', {'menu': MENU, 'title': 'Games'})
    return render(request, 'games/delete_user.html', {'title':"Delete User", 'head':'Remove user from database'})
