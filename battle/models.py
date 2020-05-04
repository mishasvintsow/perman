from django.db import models
from django.contrib.auth.models import User
import json
# Create your models here.

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bot = models.BooleanField(default=False)

class Deck(models.Model):
    location = models.CharField(default='', max_length=2)
    state = models.BooleanField(default=True) # по дефолту "живой"

class Ship(models.Model):
    state = models.BooleanField(default=True) # по дефолту "живой"

class ShipOneDeck(models.Model):
    deck1 = models.ForeignKey(Deck, on_delete=models.CASCADE)

class ShipTwoDeck(models.Model):
    deck2 = models.ForeignKey(Deck, on_delete=models.CASCADE)

class ShipThreeDeck(models.Model):
    deck3 = models.ForeignKey(Deck, on_delete=models.CASCADE)

class ShipFourDeck(models.Model):
    deck4 = models.ForeignKey(Deck, on_delete=models.CASCADE)


class Field(models.Model):
    empty_field = {}
    for i in [1,2,3,4,5,6,7,8,9,10]:
        for a in ['a','b','c','d','e','f','g','h','i','j']:
            empty_field[str(i)+a]=''
    empty_field = json.dumps(empty_field)

    map = models.TextField(default=empty_field)
    ship1d_1 = models.ForeignKey(ShipOneDeck,   null=True, on_delete=models.CASCADE, related_name='ship1d_1')
    ship1d_2 = models.ForeignKey(ShipOneDeck,   null=True, on_delete=models.CASCADE, related_name='ship1d_2')
    ship1d_3 = models.ForeignKey(ShipOneDeck,   null=True, on_delete=models.CASCADE, related_name='ship1d_3')
    ship1d_4 = models.ForeignKey(ShipOneDeck,   null=True, on_delete=models.CASCADE, related_name='ship1d_4')
    ship2d_1 = models.ForeignKey(ShipTwoDeck,   null=True, on_delete=models.CASCADE, related_name='ship2d_1')
    ship2d_2 = models.ForeignKey(ShipTwoDeck,   null=True, on_delete=models.CASCADE, related_name='ship2d_2')
    ship2d_3 = models.ForeignKey(ShipTwoDeck,   null=True, on_delete=models.CASCADE, related_name='ship2d_3')
    ship3d_1 = models.ForeignKey(ShipThreeDeck, null=True, on_delete=models.CASCADE, related_name='ship3d_1')
    ship3d_2 = models.ForeignKey(ShipThreeDeck, null=True, on_delete=models.CASCADE, related_name='ship3d_2')
    ship1d_1 = models.ForeignKey(ShipFourDeck,  null=True, on_delete=models.CASCADE, related_name='ship4d_1')

class Side(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    player_field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='player_field')
    enemy_field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='enemy_field')

class GameManager(models.Manager):
    def create_with_bot(self, player):
        playerside = Side.objects.create(player=player, player_field=Field.objects.create(), enemy_field=Field.objects.create())
        botside = Side.objects.create(player=Player.objects.get(user__username='bot'), player_field=Field.objects.create(), enemy_field=Field.objects.create())
        game = self.create(side1=botside, side2=playerside)
        return game


class Game(models.Model):
    side1 = models.ForeignKey(Side, on_delete=models.CASCADE, related_name='side1')
    side2 = models.ForeignKey(Side, on_delete=models.CASCADE, related_name='side2')
    time = models.DateTimeField(auto_now_add=True)

    objects = GameManager()

class Shot(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    location = models.CharField(default='', max_length=2)
    time = models.DateTimeField(auto_now_add=True)
