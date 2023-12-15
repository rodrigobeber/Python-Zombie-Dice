import time # for use the sleep() function
from dice import *

'''
Controls a player turn
The only public method is rollDices
'''

class Turn:

	# Lista de dices que estão com o player no turn.
	def __init__(self):
		self.brainDices = []
		self.stepDices = []
		self.brains = 0
		self.shots = 0

	# Get the dices to play (step dices + amount of dices needed from the tube)
	def __getDicesToPlay(self, tube):
		# initialize the list with stepDices
		dicesToPlay = self.stepDices[:]
		# clear the step dices list
		self.stepDices = []
		# get dices from the tube until complete 3 dices
		dicesToPlay.extend(tube.getDices(3 - len(dicesToPlay)))
		# return the dices
		return dicesToPlay

	# if the tube has less than 3 dices, return all brain dices to the tube
	def __fixTube(self, tube):
		if len(tube.dices) < 3:
			print("Returned ", len(self.brainDices), " brain dice(s) to the tube.")
			time.sleep(1)
			tube.putDices(self.brainDices)
			self.brainDices = []

	# roll 3 dices
	def rollDices(self, tube):
		# if the tube has less than 3 dices, return all brain dices to the tube
		self.__fixTube(tube)
		# get dices to play
		dicesToPlay = self.__getDicesToPlay(tube)
		# play the dices
		print("Rolled dices: ", end="")
		for dice in dicesToPlay:
			face = dice.rollDice()
			print(f"[{dice.color.name} {face.name}]", end=" ")
			if face == Face.BRAIN:
				self.brains += 1
				self.brainDices.append(dice)
			elif face == Face.STEPS:
				self.stepDices.append(dice)
			else:
				self.shots += 1
		print("")
		time.sleep(1)
