from django.db import models

class Player(models.Model):
    name=models.CharField(max_length=100)

class Game(models.Model):
    white = models.ForeignKey(Player,
                              on_delete=models.CASCADE,
                              related_name="white_games")
    black = models.ForeignKey(Player,
                              on_delete=models.CASCADE,
                              related_name="black_games")
    result= models.Charfield(max_length=7)
    pgn = models.TextField()

class Move(models.Model):
    game = models.ForeignKey(Game,
                             on_delete=models.CASCADE,
                             related_name="moves")
    move_number= models.IntegerField()
    san=models.CharField(max_length=10)


# Create your models here.
