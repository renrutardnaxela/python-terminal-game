from random import random

class Monster:
    def __init__ (self, hp, sneak, attack, defend):
        self.hp = hp
        self.sneak = sneak
        self.attack = attack
        self.defend = defend

    def monster_choice():
        monster_moves = ['sneak', 'attack', 'defend']
        monster_decides = random.choice(monster_moves)
        return monster_decides