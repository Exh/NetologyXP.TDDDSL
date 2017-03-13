class YoungerPlayer(Exception):
	pass

class Dealer(object):
	def buyChips(self, player, cash):
		if player.age < 18:
			raise YoungerPlayer

		player.cash = player.cash - cash

class Player(object):
	def __init__(self, name, age, cash):
		self._name = name
		self._age = age
		self._cash = cash

	@property
	def age(self):
		return self._age

	@property
	def cash(self):
		return self._cash

	@cash.setter
	def cash(self, v):
		self._cash = v

class PlayerBuilder(object):
	def __init__(self):
		self._name = "John Smith"
		self._age = 21
		self._cash = 0

	def create(self):
		return Player(self._name, self._age, self._cash)

	def withAge(self, age):
		self._age = age
		return self

	def withName(self, name):
		self._name = name
		return self

	def withCash(self, cash):
		self._cash = cash
		return self
