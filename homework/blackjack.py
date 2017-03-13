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


class PlayerBuilder(object):
	def __init__(self):
		self._name = "John Smith"
		self._age = 21

	def create(self):
		return Player(self._name, self._age)

	def withAge(self, age):
		self._age = age
		return self

	def withName(self, name):
		self._name = name
		return self
