import unittest
from blackjack import Player
from blackjack import Dealer
from blackjack import YoungerPlayer
from blackjack import PlayerBuilder
from blackjack import HandBuilder

class BlackJackTests(unittest.TestCase):
	def test_dealer_call_security_if_player_younger_18_years_old_buying_chips(self):
		player = PlayerBuilder().withAge(17).create()
		dealer = Dealer()
		res = False
		try:
			dealer.buyChips(player, 100)
		except YoungerPlayer:
			res = True

		self.assertEqual(res, True)


	def test_dealer_take_100_from_player_dollars(self):
		player = PlayerBuilder().withCash(100).create()
		dealer = Dealer()

		dealer.buyChips(player, 100)

		self.assertEqual(player.cash, 0)


	def test_dealer_take_100_from_player_dollars_then_he_or_she_give_100_chips_to_player(self):
		player = PlayerBuilder().withCash(100).create()
		dealer = Dealer()

		dealer.buyChips(player, 100)

		self.assertEqual(player.chips, 100)

	def test_dealer_give_me_x2_bet_prize_if_players_hand_win(self):
		player = PlayerBuilder().withChips(100).withBet(100).withHand(HandBuilder().withWin().create()).create()
		dealer = Dealer()

		dealer.settleGame(player)

		self.assertEqual(player.chips, 200)

if __name__ == '__main__':
	unittest.main()
