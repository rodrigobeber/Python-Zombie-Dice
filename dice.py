import random
from enum import Enum

class Face(Enum):
    BRAIN = "BRAIN"
    STEPS = "STEP"
    SHOT = "SHOT"

class Color(Enum):
    GREEN = 'GREEN'
    YELLOW = 'YELLOW'
    RED = 'RED'

class Dice:
    FACES_CONFIG = {
        Color.GREEN: (Face.BRAIN, Face.BRAIN, Face.BRAIN, Face.STEPS, Face.STEPS, Face.SHOT),
        Color.YELLOW: (Face.BRAIN, Face.BRAIN, Face.STEPS, Face.STEPS, Face.SHOT, Face.SHOT),
        Color.RED: (Face.BRAIN, Face.STEPS, Face.STEPS, Face.SHOT, Face.SHOT, Face.SHOT),
    }

    def __init__(self, color):
        self.color = color
        self.faces = Dice.FACES_CONFIG[color]

    def rollDice(self):
        return random.choice(self.faces)