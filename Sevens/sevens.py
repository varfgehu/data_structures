import random

number_of_players = 3
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

##########################################################################
################ CLASSES #################################################
##########################################################################

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        if self is None:
            print("CARD PASS")
            return

        if self.value == 14:
            value = "Ace"
        elif self.value == 11:
            value = "Jack"
        elif self.value == 12:
            value = "Queen"
        elif self.value == 13:
            value = "King"
        else:
            value = self.value
        print(str(value) + " of " + str(self.suit))

    def __lt__(self, other):
        t1 = self.suit, self.value
        t2 = other.suit, other.value
        return t1 < t2

    def __gt__(self, other):
        t1 = self.suit, self.value
        t2 = other.suit, other.value
        return t1 > t2

    def __eq__(self, other):
        t1 = self.suit, self.value
        t2 = other.suit, other.value
        return t1 == t2

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):    # Start for the last element, in direction to the first one
            rand = random.randint(0, i)
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]

    def draw_card(self):
        return self.cards.pop()

    def is_empty(self):
        return len(self.cards) == 0

    def __len__(self):
        return len(self.cards)

class Player(object):
    def __init__(self, name, skills = False):
        self.name = name
        self.skills = skills
        self.hand = []
        self.score = 0
        self.dealer = False
        self.next = None

    def draw(self, deck):
        if not deck.is_empty():
            self.hand.append(deck.draw_card())

    def show_hand(self):
        print(self.name + "'s cards:")
        print("################")
        for card in self.hand:
            card.show()
        print("################\n")

    def organise_hand(self):
        self.hand.sort()

    def remove_card(self, card):
        self.hand.remove(card)

    def number_of_cards_in_hand(self):
        return len(self.hand)

    def is_card_in_hand(self, card):
        return card in self.hand

    def set_for_dealer(self):
        self.dealer = True

    def remove_all_cards(self):
        self.hand = []

    def add_point(self):
        self.score += 1

    def show_score(self):
        return self.name + ": " + str(self.score)

    def pick_up_card(self, card):
        self.hand.append(card)


class Players(object):
    def __init__(self):
        self.head = None
        self.scoring = False

    def append(self, player):
        if self.head is None:
            self.head = player
            player.next = player
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = player
            player.next = self.head

    def show_game(self):
        print("Game players:")
        player = self.head
        while player:
            print(player.name)
            player = player.next
            if player == self.head:
                break
        print()

    def find_dealer(self):
        player = self.head
        while player:
            if player.dealer == True:
                return player
            player = player.next
            if player == self.head:
                break

    def clear_hands(self):
        player = self.head
        while player:
            player.remove_all_cards()
            player = player.next
            if player == self.head:
                break

    def organise_hands(self):
        player = self.head
        while player:
            player.organise_hand()
            player = player.next
            if player == self.head:
                break

    def return_player_with_7_diamonds(self):
        player = self.head
        starter_card = Card("Diamonds", 7)
        while player:
            if starter_card in player.hand:
                return player
            player = player.next

    def enable_scoring(self):
        self.scoring = True

    def is_scoring_enabled(self):
        return self.scoring

    def show_scores(self):
        player = self.head
        print("Scores:")
        while player:
            print(player.show_score())
            player = player.next
            if player == self.head:
                break
        print("")

    def shift_dealer(self):
        dealer = self.find_dealer()
        dealer.dealer = False
        dealer.next.dealer = True

class Layouts(object):
    def __init__(self):
        self.diamonds = []
        self.hearts = []
        self.spades = []
        self.clubs = []

    def show(self):
        suit_dict = {'Clubs': self.clubs, 'Diamonds': self.diamonds, 'Hearts': self.hearts, 'Spades': self.spades}
        print("    Layout")
        print("################")
        for suit_name, suit_list in suit_dict.items():
            assemble_list = []
            for suit_item in suit_list:
                assemble_list.append(replace_figures(suit_item))
            print(suit_name, assemble_list)
        print("################\n")

    def add_card(self, card):
        if card.suit == "Diamonds":
            self.diamonds.append(card.value)
            self.diamonds.sort()
        elif card.suit == "Hearts":
            self.hearts.append(card.value)
            self.hearts.sort()
        elif card.suit == "Spades":
            self.spades.append(card.value)
            self.spades.sort()
        elif card.suit == "Clubs":
            self.clubs.append(card.value)
            self.clubs.sort()
        else:
            print("Suit " + str(card.suit) + " is not valid!")
            return False

    def clear(self):
        self.diamonds = []
        self.hearts = []
        self.spades = []
        self.clubs = []

#############################################################################
######################## FUNCTIONS ##########################################
#############################################################################

def replace_figures(value):
    if value == 14:
        value = "Ace"
    elif value == 11:
        value = "Jack"
    elif value == 12:
        value = "Queen"
    elif value == 13:
        value = "King"
    else:
        pass
    return value

def place_card_to_layout(layouts, player, card):
    # print("place_card_to_layout")
    # print(player.name)
    # player.show_hand()
    # print("card:")
    # card.show()
    # print()

    # Check for "pass"
    if card is None:
        return

    player.remove_card(card)
    layouts.add_card(card)

def return_possible_cards(layouts):
    possible_cards = []
    dict = {'Hearts': layouts.hearts, 'Diamonds': layouts.diamonds, 'Spades': layouts.spades, 'Clubs': layouts.clubs}

    for suit_name, suit_list in dict.items():
        # The layout of the suit is not started, so add 7 to the list
        if len(suit_list) == 0:
            possible_cards.append(Card(suit_name, 7))
            continue

        # Find the index in values (2..14) of the firt element ([:1]) of the list, the previous index is a value for a possible card (if in range)
        for i in range(len(values)):
            if values[i] in suit_list[:1] and i > 0:
                possible_cards.append(Card(suit_name, values[i-1]))
                break

        # Find the index in values (2..14) of the last element ([:1]) of the list, the next index is a value for a possible card (if in range)
        for i in range(len(values)):
            if values[i] in suit_list[-1:] and i < 12:
                possible_cards.append(Card(suit_name, values[i+1]))
                break

    return possible_cards

def card_selection_magic(layouts, player):
    """
    Input: player (Player class)
    Output: card (Card class)
    Functionality:
    The function should select a valid card from the hand of the player,
    considering the actual layout.
    Prepare to "knock"/"pass".
    Consider:
        - the card should be valid based on the rules of the game
        - prepare for lazy and smart opponent choices
    """

    possible_cards = return_possible_cards(layouts)

    # # Print selected cards (DEBUG)
    # if len(possible_cards) == 0:
    #     return "pass"
    # print("Suitable cards:")
    # for i in range(len(possible_cards)):
    #     possible_cards[i].show()


    # Now you have all cards for a valid move
    # Filter for the hand of the actual player
    num_of_cards = len(possible_cards)
    if num_of_cards == 1:
        if player.is_card_in_hand(possible_cards[0]):
            return possible_cards[0]
        else:
            return None
    else:
        # Separate lazy and smart solutions

        # Giving some randomness to the possible cards list
        random.shuffle(possible_cards)
        # Lazy: shuffle the list of card and select the first one -> becomes random like
        if player.skills == False:
            for i in range(0, num_of_cards):
                if player.is_card_in_hand(possible_cards[i]):
                    return possible_cards[i]
            return None
        # Smart: fill a dictionary where the keys are the cards and values are the abs distance from 7, choose the highest
        else:
            max = 0
            smart_card = None
            for i in range(0, num_of_cards):
                if max <= abs(7 - possible_cards[i].value) and player.is_card_in_hand(possible_cards[i]):
                    max = abs(7 - possible_cards[i].value)
                    smart_card = possible_cards[i]

            # print("Skilled selected card:")
            # smart_card.show()
            return smart_card

def generate_card_from_input(card_input):
    """
    """
    if card_input == "pass":
        return None

    if card_input[-1] == "d":
        card_suit = "Diamonds"
    elif card_input[-1] == "h":
        card_suit = "Hearts"
    elif card_input[-1] == "s":
        card_suit = "Spades"
    else:
        card_suit = "Clubs"

    if card_input[:-1] == "a":
        card_value = 14
    elif card_input[:-1] == "j":
        card_value = 11
    elif card_input[:-1] == "q":
        card_value = 12
    elif card_input[:-1] == "k":
        card_value = 13
    else:
        card_value = int(card_input[:-1])

    return Card(card_suit, card_value)


def validate_card(layouts, player, card):
    """
    Validation steps:
    1, If "pass" was given (None card), check if any of the possible cards is in the player hand
    2, Check if the card entered by the user is in his/her hand
    3, Check if the card is suitable for the layout
    """
    possible_cards = return_possible_cards(layouts)
    if card is None:
        for possible_card in possible_cards:
            if player.is_card_in_hand(possible_card):
                return False
        return True

    if card not in player.hand:
        return False

    if card not in possible_cards:
        return False

    return True

def does_card_input_represent_card(user_input):
    if user_input == "":
        return False

    if user_input == "pass" or user_input[-1] in ["d", "h", "s", "c"] and user_input[:-1].lower() in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k", "a"]:
        return True
    return False

def deal_cards(players, deck):
    player = players.find_dealer()
    print("Dealer: " + player.name)
    while not deck.is_empty():
        player.next.draw(deck)
        player = player.next

def ask_player_name():
    while True:
        user_input = input("Please enter a name: ")
        if user_input == "":
            print("Player name can not be empty!")
            continue
        return user_input

def ask_yes_no(string):
    while True:
        user_input = input(string)
        if user_input.lower() == "y" or user_input.lower() == "n":
            return user_input
        else:
            print("Not valid answer!")
            continue

################################################################################
############################ MAIN ##############################################
################################################################################
def main():
    # Create the deck of the 52 cards and shuffle them
    deck = Deck()
    deck.shuffle()

    # Create players
    players = Players()
    player_name = ask_player_name()
    user = Player(player_name)
    lazy = Player("Lazy")
    smart  = Player("Smart", True)
    players.append(user)
    players.append(lazy)
    players.append(smart)
    players.show_game()

    # Create layout for the layed down cards
    layouts = Layouts()

    # Scoring decision and setting
    user_scoring_choice = ask_yes_no("Would you like to collect scores? (y/n)\n")
    if user_scoring_choice.lower() == "y":
        players.enable_scoring()

    # Handle dealing
    user_dealer_choice = ask_yes_no("Would you like to be the first dealer? (y/n)\n")
    if user_dealer_choice.lower() == "y":
        user.set_for_dealer()
    else:
        lazy.set_for_dealer()

    deal_cards(players, deck)
    players.organise_hands()
    while True:
        # Starting the game, the first round with 7 of Diamonds is generated
        player_with_action = players.return_player_with_7_diamonds()
        print("The player with the 7 of Diamonds stars the Game:", player_with_action.name)

        place_card_to_layout(layouts,player_with_action, Card("Diamonds", 7))
        player_with_action = player_with_action.next

        while True:
            if player_with_action == user:
                # Create an input to allow the user to enter his/her selected card
                print("\n\nYour turn: " + str(player_with_action.name) + "\n")
                layouts.show()
                player_with_action.show_hand()
                print("Select a card from your hand!\n")
                while True:
                    card_input = input("")
                    if not does_card_input_represent_card(card_input):
                        print("Not a valid input for card.\n(Selected card format: For 7 of Diamonds enter 7d, for King of Heart enter kh)\nPlease try again!")
                        continue
                    selected_card = generate_card_from_input(card_input)
                    if validate_card(layouts, player_with_action, selected_card):
                        break
                    else:
                        print("Not a valid choice now.\n")
            else:
                selected_card = card_selection_magic(layouts, player_with_action)

            print(player_with_action.name + "'s action:")
            if selected_card is None:
                print("PASS")
            else:
                selected_card.show()
                place_card_to_layout(layouts, player_with_action, selected_card)

            if player_with_action.number_of_cards_in_hand() == 0:
                print("The winner is: ", player_with_action.name)
                if players.is_scoring_enabled():
                    player_with_action.add_point()
                break

            player_with_action = player_with_action.next

        if players.is_scoring_enabled():
            players.show_scores()

        user_input = ask_yes_no("Would you like to play again? (y/n)")
        if user_input.lower() == "n":
            break
        else:
            # Build Deck
            deck.build()
            # Shuffle cards
            deck.shuffle()
            # Clear layouts
            layouts.clear()
            # Clear player hands
            players.clear_hands()
            # Shift dealer
            players.shift_dealer()
            # Deal cards, organise hands
            deal_cards(players, deck)
            players.organise_hands()

    print("Thank you for playing, try again soon!")

if __name__ == '__main__':
    main()
