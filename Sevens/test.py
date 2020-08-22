import unittest

from sevens_with_skills import *

class TestDeck(unittest.TestCase):

    def test_deck_is_not_empty(self):
        deck = Deck()
        self.assertFalse(deck.is_empty())

    def test_deck_creates_52_cards(self):
        deck = Deck()
        self.assertEqual(len(deck), 52)

    def test_shuffle_deck(self):
        deck = Deck()
        self.assertNotEqual(deck, deck.shuffle())

    def test_draw_card(self):
        deck = Deck()
        deck.draw_card()
        self.assertEqual(len(deck), 51)


class TestCard(unittest.TestCase):
    def test_create_card_suit_test(self):
        card = Card("Diamond", 7)
        self.assertEqual(card.suit, "Diamond")
        self.assertEqual(card.value, 7)

class TestPlayer(unittest.TestCase):
    def test_player(self):
        player = Player("Name", False)
        self.assertEqual(player.name, "Name")
        self.assertEqual(player.skills, False)
        self.assertEqual(player.score, 0)
        self.assertEqual(player.dealer, False)
        self.assertEqual(player.next, None)

    def test_player_draws(self):
        deck = Deck()
        player = Player("Name", False)
        player.draw(deck)
        self.assertEqual(len(player.hand), 1)
        self.assertEqual(len(deck), 51)

    def test_organise_player_hand(self):
        player = Player("Name", False)
        hearts_7_card = Card("Hearts", 7)
        hearts_8_card = Card("Hearts", 8)
        diamonds_6_card = Card("Diamonds", 6)
        diamonds_7_card = Card("Diamonds", 7)
        clubs_5_card = Card("Clubs", 5)
        clubs_8_card = Card("Clubs", 8)
        spades_10_card = Card("Spades", 10)
        spades_14_card = Card("Spades", 14)
        player.hand.append(hearts_8_card)
        player.hand.append(hearts_7_card)
        player.hand.append(diamonds_7_card)
        player.hand.append(diamonds_6_card)
        player.hand.append(clubs_5_card)
        player.hand.append(clubs_8_card)
        player.hand.append(spades_14_card)
        player.hand.append(spades_10_card)
        player.organise_hand()
        self.assertEqual(player.hand, [ clubs_5_card, clubs_8_card, diamonds_6_card, diamonds_7_card, hearts_7_card, hearts_8_card, spades_10_card, spades_14_card ] )

    def test_remove_card(self):
        player = Player("Name", False)
        hearts_7_card = Card("Hearts", 7)
        hearts_8_card = Card("Hearts", 8)
        player.hand.append(hearts_8_card)
        player.hand.append(hearts_7_card)
        self.assertEqual(len(player.hand), 2)
        player.remove_card(hearts_7_card)
        self.assertEqual(len(player.hand), 1)
        self.assertEqual(player.hand, [hearts_8_card])

    def test_is_card_in_hand(self):
        pass

if __name__ == '__main__':
    unittest.main()
