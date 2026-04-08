from django.shortcuts import render
from rest_framework import viewsets
from .models import Game, Player
from .serializers import GameSerializer, PlayerSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
# Create your views here.
