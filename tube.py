from dice import *
import random

class Tube:

	# tube initialization with 13 dices (6 greens, 4 yellows, and 3 reds)
	def __init__(self):
		self.dices = [Dice(Color.GREEN) for _ in range(6)]
		self.dices.extend([Dice(Color.YELLOW) for _ in range(4)])
		self.dices.extend([Dice(Color.RED) for _ in range(3)])

	# ramdonly get 'qty' dices from the tube
	def getDices(self, qty):
		dices = []
		for i in range(qty):
			dice = random.choice(self.dices)
			self.dices.remove(dice)
			dices.append(dice)
		return dices

	# put dices in the tube
	def putDices(self, dices):
		self.dices.extend(dices)

