import unittest
from blackjack import Player
from blackjack import Dealer
from blackjack import YoungerPlayer

class BlackJackTests(unittest.TestCase):
	def test_dealer_call_security_if_player_younger_18_years_old_buying_chips(self):
		player = Player("Peter", 17)
		dealer = Dealer()
		res = False
		try:
			dealer.buyChips(player, 100)
		except YoungerPlayer:
			res = True

		self.assertEqual(res, True)

if __name__ == '__main__':
	unittest.main()
