from django.shortcuts import render, redirect
from .models import Player, Game
from django.db.models import Q
# Create your views here.

def index(request):
    games = Game.objects.filter(Q(side1__player__user=request.user) | Q(side2__player__user=request.user))
    return render(request, 'battle/index.html', {'games' : games})

def create(request):
    player = Player.objects.get(user=request.user)
    game = Game.objects.create_with_bot(player)
    return redirect('/')