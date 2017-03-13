class YoungerPlayer(Exception):
	pass

class Dealer(object):
	def buyChips(self, player, cash):
		if player.age < 18:
			raise YoungerPlayer

class Player(object):
	def __init__(self, name, age):
		self._name = name
		self._age = age

	@property
	def age(self):
		return self._age
