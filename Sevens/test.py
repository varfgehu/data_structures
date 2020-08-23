import unittest

from sevens import *

class TestDeckClass(unittest.TestCase):

    def test_deck_is_not_empty(self):
        d = Deck()
        self.assertFalse(d.is_empty())

    def test_deck_creates_52_cards(self):
        d = Deck()
        self.assertEqual(len(d), 52)

    def test_shuffle_deck(self):
        d = Deck()
        self.assertNotEqual(d, d.shuffle())

    def test_draw_card(self):
        d = Deck()
        d.draw_card()
        self.assertEqual(len(d), 51)


class TestCardClass(unittest.TestCase):
    def test_create_card_suit_test(self):
        c = Card("Diamond", 7)
        self.assertEqual(c.suit, "Diamond")
        self.assertEqual(c.value, 7)

    def test_card_less_than(self):
        d7_card = Card("Diamond", 7)
        d8_card = Card("Diamond", 8)
        c8_card = Card("Clubs", 7)
        self.assertTrue(d7_card < d8_card)
        self.assertFalse(d7_card < c8_card)
        self.assertTrue(c8_card < d7_card)

    def test_card_greater_than(self):
        d7_card = Card("Diamond", 7)
        d8_card = Card("Diamond", 8)
        c8_card = Card("Clubs", 7)
        self.assertTrue(d7_card < d8_card)
        self.assertFalse(d7_card < c8_card)
        self.assertTrue(c8_card < d7_card)

    def test_card_equal_to(self):
        d7_card = Card("Diamond", 7)
        d8_card = Card("Diamond", 8)
        c8_card = Card("Clubs", 7)
        self.assertFalse(d7_card == d8_card)
        self.assertFalse(d8_card == c8_card)
        self.assertTrue(d7_card == d7_card)

class TestPlayerClass(unittest.TestCase):
    def test_create_player(self):
        p = Player("Name")
        self.assertEqual(p.name, "Name")
        self.assertEqual(p.skills, False)
        self.assertEqual(p.score, 0)
        self.assertEqual(p.dealer, False)
        self.assertEqual(p.next, None)
        p_with_skill = Player("Skill", True)
        self.assertTrue(p_with_skill.skills)

    def test_player_draws(self):
        d = Deck()
        p = Player("Name", False)
        p.draw(d)
        self.assertEqual(len(p.hand), 1)
        self.assertEqual(len(d), 51)

    def test_player_pick_up_card(self):
        p = Player("Name")
        d6_card = Card("Diamonds", 6)
        p.pick_up_card(d6_card)
        self.assertEqual(p.hand[0], d6_card)

    def test_organise_player_hand(self):
        p = Player("Name", False)
        h7_card = Card("Hearts", 7)
        h8_card = Card("Hearts", 8)
        d6_card = Card("Diamonds", 6)
        d7_card = Card("Diamonds", 7)
        c5_card = Card("Clubs", 5)
        c8_card = Card("Clubs", 8)
        s10_card = Card("Spades", 10)
        s14_card = Card("Spades", 14)
        p.pick_up_card(h8_card)
        p.pick_up_card(h7_card)
        p.pick_up_card(d7_card)
        p.pick_up_card(d6_card)
        p.pick_up_card(c5_card)
        p.pick_up_card(c8_card)
        p.pick_up_card(s14_card)
        p.pick_up_card(s10_card)
        p.organise_hand()
        self.assertEqual(p.hand, [ c5_card, c8_card, d6_card, d7_card, h7_card, h8_card, s10_card, s14_card ] )

    def test_remove_card(self):
        p = Player("Name", False)
        h7_card = Card("Hearts", 7)
        h8_card = Card("Hearts", 8)
        p.pick_up_card(h8_card)
        p.pick_up_card(h7_card)
        self.assertEqual(len(p.hand), 2)
        p.remove_card(h7_card)
        self.assertEqual(len(p.hand), 1)
        self.assertEqual(p.hand, [h8_card])

    def test_is_card_in_hand(self):
        p = Player("Name")
        d7_card = Card("Diamonds", 7)
        d8_card = Card("Diamonds", 7)
        p.pick_up_card(d7_card)
        p.pick_up_card(d8_card)
        self.assertTrue(p.is_card_in_hand(d8_card))

    def test_player_set_for_dealer(self):
        p = Player("Name")
        self.assertFalse(p.dealer)
        p.set_for_dealer()
        self.assertTrue(p.dealer)

    def test_player_remove_cards(self):
        p = Player("Name")
        d7_card = Card("Diamonds", 7)
        d8_card = Card("Diamonds", 7)
        p.pick_up_card(d7_card)
        p.pick_up_card(d8_card)
        p.remove_all_cards()
        self.assertEqual(len(p.hand), 0)

    def test_player_add_point(self):
        p = Player("Name")
        p.add_point()
        p.add_point()
        self.assertEqual(p.score, 2)

    def test_player_show_score(self):
        p = Player("Name")
        p.add_point()
        p.add_point()
        p.add_point()
        self.assertEqual(p.show_score(), "Name: 3")

    def test_player_return_player_name(self):
        p = Player("Name")
        self.assertEqual(p.get_player_name(), "Name")

class TestGameClass(unittest.TestCase):
    def test_game_init(self):
        g = Game()
        self.assertIsNone(g.head)
        self.assertFalse(g.scoring)

    def test_game_append(self):
        g = Game()
        p1 = Player("Name")
        g.append(p1)
        self.assertEqual(g.head, p1)
        self.assertEqual(p1.next, p1)

    def test_game_append_2(self):
        g = Game()
        p1 = Player("Name")
        p2 = Player("Name2")
        g.append(p1)
        g.append(p2)
        self.assertEqual(g.head, p1)
        self.assertEqual(p1.next, p2)
        self.assertEqual(p2.next, p1)

    def test_game_find_dealer(self):
        g = Game()
        p1 = Player("Name")
        p2 = Player("Name2")
        g.append(p1)
        g.append(p2)
        p2.set_for_dealer()
        self.assertEqual(g.find_dealer(), p2)

    def test_game_clear_hands(self):
        g = Game()
        p1 = Player("Name")
        p2 = Player("Name2")
        h7_card = Card("Hearts", 7)
        h8_card = Card("Hearts", 8)
        d6_card = Card("Diamonds", 6)
        d7_card = Card("Diamonds", 7)
        p1.pick_up_card(h8_card)
        p1.pick_up_card(h7_card)
        p2.pick_up_card(d7_card)
        p2.pick_up_card(d6_card)
        g.append(p1)
        g.append(p2)
        self.assertEqual(len(p1.hand), 2)
        self.assertEqual(len(p1.hand), 2)
        g.clear_hands()
        self.assertEqual(len(p1.hand), 0)
        self.assertEqual(len(p1.hand), 0)

    def test_game_organise_hands(self):
        g = Game()
        p1 = Player("Name")
        p2 = Player("Name2")
        h7_card = Card("Hearts", 7)
        h8_card = Card("Hearts", 8)
        d6_card = Card("Diamonds", 6)
        d7_card = Card("Diamonds", 7)
        p1.pick_up_card(h8_card)
        p1.pick_up_card(d6_card)
        p2.pick_up_card(h7_card)
        p2.pick_up_card(d7_card)
        g.append(p1)
        g.append(p2)
        g.organise_hands()
        self.assertEqual(p1.hand, [d6_card, h8_card])
        self.assertEqual(p2.hand, [d7_card, h7_card])

    def test_game_return_player_with_7_diamonds(self):
        g = Game()
        p1 = Player("Name")
        p2 = Player("Name2")
        h7_card = Card("Hearts", 7)
        h8_card = Card("Hearts", 8)
        d6_card = Card("Diamonds", 6)
        d7_card = Card("Diamonds", 7)
        p1.pick_up_card(h8_card)
        p1.pick_up_card(d6_card)
        p2.pick_up_card(h7_card)
        p2.pick_up_card(d7_card)
        g.append(p1)
        g.append(p2)
        self.assertEqual(g.return_player_with_7_diamonds(), p2)

    def test_game_enable_scoring(self):
        g = Game()
        g.enable_scoring()
        self.assertTrue(g.scoring)

    def test_game_is_scoring_enabled(self):
        g = Game()
        g.enable_scoring()
        self.assertTrue(g.is_scoring_enabled())

    def test_game_shift_dealer(self):
        g = Game()
        p1 =  Player("Name1")
        p2 =  Player("Name2")
        p3 =  Player("Dealer")
        p1.set_for_dealer()
        g.append(p1)
        g.append(p2)
        g.append(p3)
        g.shift_dealer()
        self.assertEqual(g.find_dealer(), p2)

class TestLayoutsClass(unittest.TestCase):
    def test_layouts_init(self):
        l = Layouts()
        self.assertEqual(l.diamonds, [])
        self.assertEqual(l.hearts, [])
        self.assertEqual(l.spades, [])
        self.assertEqual(l.clubs, [])

    def test_layouts_add_card(self):
        l = Layouts()
        h7_card = Card("Hearts", 7)
        d6_card = Card("Diamonds", 6)
        c5_card = Card("Clubs", 5)
        s2_card = Card("Spades", 2)
        s10_card = Card("Spades", 10)
        l.add_card(h7_card)
        self.assertEqual(l.diamonds, [])
        self.assertEqual(l.hearts, [7])
        self.assertEqual(l.spades, [])
        self.assertEqual(l.clubs, [])

        l.add_card(d6_card)
        self.assertEqual(l.diamonds, [6])
        self.assertEqual(l.hearts, [7])
        self.assertEqual(l.spades, [])
        self.assertEqual(l.clubs, [])

        l.add_card(c5_card)
        self.assertEqual(l.diamonds, [6])
        self.assertEqual(l.hearts, [7])
        self.assertEqual(l.spades, [])
        self.assertEqual(l.clubs, [5])

        l.add_card(s10_card)
        self.assertEqual(l.diamonds, [6])
        self.assertEqual(l.hearts, [7])
        self.assertEqual(l.spades, [10])
        self.assertEqual(l.clubs, [5])

        l.add_card(s2_card)
        self.assertEqual(l.diamonds, [6])
        self.assertEqual(l.hearts, [7])
        self.assertEqual(l.spades, [2,10])
        self.assertEqual(l.clubs, [5])

    def test_layouts_clear(self):
        l = Layouts()
        h7_card = Card("Hearts", 7)
        d6_card = Card("Diamonds", 6)
        c5_card = Card("Clubs", 5)
        s2_card = Card("Spades", 2)
        s10_card = Card("Spades", 10)
        l.add_card(h7_card)
        l.add_card(d6_card)
        l.add_card(c5_card)
        l.add_card(s10_card)
        l.add_card(s2_card)
        l.clear()
        self.assertEqual(l.diamonds, [])
        self.assertEqual(l.hearts, [])
        self.assertEqual(l.spades, [])
        self.assertEqual(l.clubs, [])


class TestFunctions(unittest.TestCase):
    def test_replace_figures(self):
        self.assertEqual(replace_figures(14), "Ace")
        self.assertEqual(replace_figures(11), "Jack")
        self.assertEqual(replace_figures(12), "Queen")
        self.assertEqual(replace_figures(13), "King")
        self.assertEqual(replace_figures(2), 2)

    def test_place_card_to_layout(self):
        layouts = Layouts()
        player = Player("Name")
        h7_card = Card("Hearts", 7)
        d6_card = Card("Diamonds", 6)
        player.pick_up_card(h7_card)
        player.pick_up_card(d6_card)
        place_card_to_layout(layouts, player, d6_card)
        self.assertEqual(layouts.diamonds, [6])
        self.assertEqual(layouts.hearts, [])
        self.assertEqual(layouts.spades, [])
        self.assertEqual(layouts.clubs, [])
        self.assertEqual(player.hand, [h7_card])

    def test_place_none_to_layout(self):
        l = Layouts()
        p = Player("Name")
        h7_card = Card("Hearts", 7)
        d6_card = Card("Diamonds", 6)
        p.pick_up_card(h7_card)
        p.pick_up_card(d6_card)
        place_card_to_layout(l, p, None)
        self.assertEqual(l.diamonds, [])
        self.assertEqual(l.hearts, [])
        self.assertEqual(l.spades, [])
        self.assertEqual(l.clubs, [])
        self.assertEqual(p.hand, [h7_card, d6_card])

    def test_return_possible_cards_empty_layout(self):
        l = Layouts()
        h7_card = Card("Hearts", 7)
        d7_card = Card("Diamonds", 7)
        s7_card = Card("Spades", 7)
        c7_card = Card("Clubs", 7)
        self.assertEqual(return_possible_cards(l), [h7_card, d7_card, s7_card, c7_card] )

    def test_return_possible_cards_main_cases(self):
        l = Layouts()
        h7_card = Card("Hearts", 7)
        d6_card = Card("Diamonds", 6)
        d7_card = Card("Diamonds", 7)
        d8_card = Card("Diamonds", 8)
        s7_card = Card("Spades", 7)
        c7_card = Card("Clubs", 7)
        l.add_card(d7_card)
        self.assertEqual(return_possible_cards(l), [h7_card, d6_card, d8_card, s7_card ,c7_card])

    def test_return_possible_cards_edge_cases(self):
        l = Layouts()
        for i in range(2,14 + 1):
            l.add_card(Card("Diamonds", i))
        h7_card = Card("Hearts", 7)
        s7_card = Card("Spades", 7)
        c7_card = Card("Clubs", 7)
        self.assertEqual(return_possible_cards(l), [h7_card, s7_card ,c7_card])

    def test_card_selection_magic_lazy(self):
        l = Layouts()
        p = Player("Lazy")
        d7_card = Card("Diamonds", 7)
        s7_card = Card("Spades", 7)
        c7_card = Card("Clubs", 7)
        l.add_card(d7_card)
        p.pick_up_card(c7_card)
        p.pick_up_card(s7_card)
        self.assertIn(card_selection_magic(l, p), [c7_card, s7_card])

    def test_card_selection_magic_smart(self):
        l = Layouts()
        p = Player("Smart", True)
        for i in range(2,13 + 1):
            l.add_card(Card("Diamonds", i))

        c7_card = Card("Clubs", 7)
        da_card = Card("Diamonds", 14)
        p.pick_up_card(c7_card)
        p.pick_up_card(da_card)
        self.assertEqual(card_selection_magic(l, p), da_card)

    def test_generate_card_from_input(self):
        self.assertEqual(generate_card_from_input("pass"), None)
        self.assertEqual(generate_card_from_input("ad"), Card("Diamonds", 14))
        self.assertEqual(generate_card_from_input("jh"), Card("Hearts", 11))
        self.assertEqual(generate_card_from_input("qs"), Card("Spades", 12))
        self.assertEqual(generate_card_from_input("kc"), Card("Clubs", 13))
        self.assertEqual(generate_card_from_input("10d"), Card("Diamonds", 10))

    def test_validate_card_pass_false(self):
        l = Layouts()
        p = Player("Smart", True)
        for i in range(2,13 + 1):
            l.add_card(Card("Diamonds", i))

        c7_card = Card("Clubs", 7)
        ca_card = Card("Clubs", 14)
        p.pick_up_card(c7_card)
        p.pick_up_card(ca_card)
        self.assertEqual(validate_card(l, p, None), False)

    def test_validate_card_pass_true(self):
        l = Layouts()
        p = Player("Smart", True)
        for i in range(2,13 + 1):
            l.add_card(Card("Diamonds", i))

        c8_card = Card("Clubs", 8)
        ca_card = Card("Clubs", 14)
        p.pick_up_card(c8_card)
        p.pick_up_card(ca_card)
        self.assertEqual(validate_card(l, p, None), True)

    def test_validate_card_card_not_in_hand(self):
        l = Layouts()
        p = Player("Smart", True)
        for i in range(2,13 + 1):
            l.add_card(Card("Diamonds", i))

        c8_card = Card("Clubs", 8)
        ca_card = Card("Clubs", 14)
        p.pick_up_card(c8_card)
        p.pick_up_card(ca_card)
        self.assertEqual(validate_card(l, p, Card("Clubs", 7)), False)

    def test_validate_card_card_not_in_possible_cards(self):
        l = Layouts()
        p = Player("Smart", True)
        for i in range(2,13 + 1):
            l.add_card(Card("Diamonds", i))

        c8_card = Card("Clubs", 8)
        ca_card = Card("Clubs", 14)
        p.pick_up_card(c8_card)
        p.pick_up_card(ca_card)
        self.assertEqual(validate_card(l, p, Card("Clubs", 9)), False)

    def test_does_card_input_represent_card(self):
        self.assertEqual(does_card_input_represent_card(""), False)
        self.assertEqual(does_card_input_represent_card("pass"), True)
        self.assertEqual(does_card_input_represent_card("2d"), True)
        self.assertEqual(does_card_input_represent_card("3h"), True)
        self.assertEqual(does_card_input_represent_card("4s"), True)
        self.assertEqual(does_card_input_represent_card("5c"), True)
        self.assertEqual(does_card_input_represent_card("6d"), True)
        self.assertEqual(does_card_input_represent_card("7h"), True)
        self.assertEqual(does_card_input_represent_card("8s"), True)
        self.assertEqual(does_card_input_represent_card("9c"), True)
        self.assertEqual(does_card_input_represent_card("10c"), True)
        self.assertEqual(does_card_input_represent_card("jh"), True)
        self.assertEqual(does_card_input_represent_card("qs"), True)
        self.assertEqual(does_card_input_represent_card("kc"), True)
        self.assertEqual(does_card_input_represent_card("ac"), True)
        self.assertEqual(does_card_input_represent_card("hj"), False)
        self.assertEqual(does_card_input_represent_card("c5"), False)
        self.assertEqual(does_card_input_represent_card("asdf"), False)

    def test_deal_cards(self):
        d = Deck()
        g = Game()
        p1 =  Player("Name1")
        p2 =  Player("Name2")
        p3 =  Player("Dealer")
        p3.set_for_dealer()
        g.append(p1)
        g.append(p2)
        g.append(p3)
        deal_cards(g, d)
        self.assertEqual(len(p1.hand), 18)
        self.assertEqual(len(p2.hand), 17)
        self.assertEqual(len(p2.hand), 17)


if __name__ == '__main__':
    unittest.main()
