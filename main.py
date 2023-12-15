from welcome import *
from initialinput import *
from confirm import *
from game import *

Welcome.sayWelcome()
qty = InitialInput.readNumOfPlayers()
players = InitialInput.readPlayerList(qty)
initialPlayer = InitialInput.readInitialPlayer(players)
game = Game(players)

while True:
    winner = game.play(initialPlayer)
    if confirm('\n\nRestart the game Y/N?'):
        initialPlayer = winner
    else:
        break

print('\n\nfinished.')