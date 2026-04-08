from rest_framework import serializers
from .models import Game, Move, Player

class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields=["move_number","san"]

class GameSerializer(serializers.ModelSerializer):
    moves = MoveSerializer(many=True, read_only = True)
    white = serializers.StringRelatedField()
    black = serializers.StringRelatedField()
    class Meta:
        model = Game
        fields = ['id', 'white', 'black', 'result', 'pgn', 'moves']


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name']

