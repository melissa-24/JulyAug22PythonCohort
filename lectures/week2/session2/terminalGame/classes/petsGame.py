import random
from .player import *
from .pet import *
from .trick import *

class PetsGame:
    def __init__(self):
        self.leave = 0



    def start(self):
        message = print("Lets get started\n\n")
        petInput = str(input('Please give your pet character a name\n\n'))
        pet = Pet(petInput)
        game = True
        while game:
            tricks()