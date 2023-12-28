from math import floor, sqrt
from random import randint
from time import sleep
from display import *
import os

class player():
    '''a player eg. user and bot'''
    names = []
    players = []
    def __init__(self, name: str, health: int, attack: int, defense: int, stamina: int):
        self.__name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.stamina = stamina
        self.silenced = (False, 1)

        # add player to the list of players
        player.players.append(self)
        player.names.append(self.__name)
    
    @property
    def name(self):
        return self.__name
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.health}, {self.attack}, {self.defense}, {self.stamina})"
    
    # checks if player is dead
    def is_dead(self):
        if self.health <= 0:
            print(f"{self.name} has died!")
            return True
        else:
            return False

    # checks what type of move the opponent does
    def move_recieved(self, move_info):
        if move_info[0]:
            self.debuff(move_info)
        else:
            self.calculate_damage(move_info)

    # adds silenced status
    def debuff(self, silence):
        self.status = silence
    
    # calculates damage
    def calculate_damage(self, move_info):
        i, attack, base_damage = move_info
        total_damage = floor(sqrt(attack / self.defense) * base_damage * (randint(8, 10) / 10))
        self.takes_damage(total_damage)
    
    def takes_damage(self, damage: int):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    # player moveset
    def silence(self):
        return (True, 0)
    
    def normal_attack(self):
        return (False, self.attack, 20)
    
    # makes player choose a move
    def choose(self):
        choices = {"attack": 0, "silence": 1, "signature": 2}
        chocie = input("Choose a move: ").lower()
        

    def turn_end(self):
        status, turns = self.silenced

        if turns == 0:
            self.silenced = (False, 1)
        elif status and turns > 1:
            self.silenced = (True, turns - 1)
        elif status and turns == 1:
            self.silenced = (False, 1)
            

class assasin(player):
    pass
