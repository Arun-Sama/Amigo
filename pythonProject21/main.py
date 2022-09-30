from fastapi import FastAPI
from random import *

app = FastAPI()


class Weapon(str):
    rock = 'rock'
    paper = 'paper'
    scissor = 'scissor'


@app.get('/')
def shoot(weapon: Weapon):
    game_key = {
        ('rock', 'rock'): "Its a tie",
        ('rock', 'paper'): "You lost",
        ('rock', 'scissor'): "You won",
        ('paper', 'paper'): "Its a tie",
        ('paper', 'scissor'): "You lost",
        ('paper', 'rock'): "You won",
        ('scissor', 'scissor'): "Its a tie",
        ('scissor', 'rock'): "You lost",
        ('scissor', 'paper'): "You won",
    }

    weapons = ['rock', 'paper', 'scissor']
    opp_weapon = weapons[randrange(0, 3)]
    message = game_key[(weapon, opp_weapon)]
    result = {'user_weapon': weapon, 'opponent_weapon': opp_weapon, 'message': message}

    return result
