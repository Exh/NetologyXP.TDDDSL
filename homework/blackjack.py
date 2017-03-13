class YoungerPlayer(Exception):
	pass

class Dealer(object):
	def buyChips(self, player, cash):
		if player.age < 18:
			raise YoungerPlayer

		player.cash -= cash
		player.chips +=  cash

	def settleGame(self, player):
		if player.hand.isWin:
			player.chips += player.bet

class Player(object):
	def __init__(self, name, age, cash, chips, bet, hand):
		self._name = name
		self._age = age
		self._cash = cash
		self._chips = chips
		self._bet = bet
		self._hand = hand


	@property
	def age(self):
		return self._age

	@property
	def cash(self):
		return self._cash

	@cash.setter
	def cash(self, v):
		self._cash = v

	@property
	def chips(self):
		return self._chips

	@chips.setter
	def chips(self, v):
		self._chips = v

	@property
	def hand(self):
		return self._hand

	@hand.setter
	def hand(self, v):
		self._hand = v

	@property
	def bet(self):
		return self._bet

	@bet.setter
	def bet(self, v):
		self._bet = v

class PlayerBuilder(object):
	def __init__(self):
		self._name = "John Smith"
		self._age = 21
		self._cash = 0
		self._chips = 0
		self._bet = 0
		self._hand = None

	def create(self):
		return Player(self._name, self._age, self._cash, self._chips, self._bet, self._hand)

	def withAge(self, age):
		self._age = age
		return self

	def withName(self, name):
		self._name = name
		return self

	def withCash(self, cash):
		self._cash = cash
		return self

	def withChips(self, chips):
		self._chips = chips
		return self

	def withBet(self, bet):
		self._bet = bet
		return self

	def withHand(self, hand):
		self._hand = hand
		return self

class Hand(object):
	def __init__(self, isWin):
		self._isWin = isWin

	@property
	def isWin(self):
		return self._isWin


class HandBuilder(object):
	def __init__(self):
		self._isWin = False

	def withWin(self):
		self._isWin = True
		return self

	def create(self):
		return Hand(self._isWin)
