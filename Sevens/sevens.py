import random

number_of_players = 3
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
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
                # print(str(value) + " of " + str(suit))

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

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.dealer = False
        self.next = None

    def draw(self, deck):
        if not deck.is_empty():
            self.hand.append(deck.draw_card())

    def show_hand(self):
        print(self.name + " cards:")
        for card in self.hand:
            card.show()

    def organise_hand(self):
        sorted_cards = []
        self.hand.sort()

    def remove_card(self, card):
        self.hand.remove(card)


class Players(object):
    def __init__(self):
        self.head = None

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
        player = self.head
        while player:
            print(player.name)
            player = player.next
            if player == self.head:
                break

    def find_dealer(self):
        player = self.head
        while player:
            if player.dealer == True:
                return player
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

    def do_we_have_a_winner(self):
        """
        If one player do not have cards in hand, return the player
        """
        player = self.head
        while player:
            if len(player.hand) == 0:
                return player
            player = player.next
        return False

class Layouts(object):
    def __init__(self):
        self.diamonds = []
        self.hearts = []
        self.spades = []
        self.clubs = []

    def show(self):
        print("Diamonds: " + str(self.diamonds))
        print("Hearts: " + str(self.hearts))
        print("Spades: " + str(self.spades))
        print("Clubs: " + str(self.clubs))

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


def place_card_to_layout(player, card):
    # TODO!!!!!!!!!!!!!!!!!!!!!!
    # Check is it valid
    # 1, Does the user have the card
    # 2, Dose the card fit in the actual layout
    # Take actions if both are TRUE

    # remove card from the hand of the player
    player.remove_card(card)
    # add to the layout
    # sort the layout
    layouts.add_card(card)


def card_selection_magic(player):
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
    # Collect all possible cards to play
    # possible_cards = []
    # for i in len(range(values)):
    #     if values[i] == layouts.diamonds

    pass

def generate_card_from_input(card_input):
    """
    Create a card instance from the card input
            if self.value == 14:
                value = "Ace"
            elif self.value == 11:
                value = "Jack"
            elif self.value == 12:
                value = "Queen"
            elif self.value == 13:
                value = "King"
    """
    suit_code = card_input[-1]
    if suit_code == "d":
        suit = "Diamonds"
    elif suit_code == "h":
        suit = "Hearts"
    elif suit_code == "s":
        suit = "Spades"
    elif suit_code == "c":
        siut = "Clubs"
    else:
        print("Unknown suit code input!")
        return False

    value_code = card_input[:-1]
    if value_code == "a":
        value = 14
    elif value_code == "j":
        value = 11
    elif value_code == "q":
        value = 12
    elif value_code == "k":
        value = 13
    else:
        value = value_code

    return Card(suit, value)



# Create the deck of the 52 cards
deck = Deck()
# deck.show()

# Shuffle the cards
deck.shuffle()
print()
players = Players()
player_name = input("Please enter a name!")
user = Player(player_name)
lazy = Player("Lazy")
smart  = Player("Smart")
players.append(user)
players.append(lazy)
players.append(smart)
players.show_game()
user_dealer_choice = input("Would you like to be the first dealer? (y/n)")
print(user_dealer_choice)

if user_dealer_choice == "y":
    user.dealer = True
else:
    lazy.dealer = True

player = players.find_dealer()
print("Dealer: " + player.name)
while not deck.is_empty():
    player.next.draw(deck)
    player = player.next

# print()
# user.show_hand()
# print()
# lazy.show_hand()
# print()
# smart.show_hand()
# print()

# lazy.organise_hand()
# lazy.show_hand()
# smart.organise_hand()
# smart.show_hand()

user.organise_hand()
user.show_hand()

# Create layout for the layed down cards
layouts = Layouts()
layouts.show()

# Start the game
# The game starts with placing the seven of Diamonds
player_with_action = players.return_player_with_7_diamonds()
print("The Game starts with 7 of Diamonds")
print("The following player starts the game: " + str(player_with_action.name))

place_card_to_layout(player_with_action, Card("Diamonds", 7))
player_with_action = player_with_action.next
# layouts.show()

while True:
    # The actual player select a card to place

    if player_with_action == user:
        # Create an input to allow the user to enter his/her selected card
        print("Your turn: " + str(player_with_action.name))
        layouts.show()
        player_with_action.show_hand()
        card_input = input("Select a card from your hand!\n(Selected card format: For 7 of Diamonds enter 7d, for King of Heart enter kh)")
        selected_card = generate_card_from_input(card_input)
    else:
        selected_card = card_selection_magic(player_with_action)

    selected_card.show()
    # place_card_to_layout(player_with_action, selected_card)
    # player_with_action = player_with_action.next

    if players.do_we_have_a_winner() == True:
        # The current game is over
        # Count points or handle money....
        # Ask user what he/she wants.. ( play again, quit)
        pass






































# Organise user hand first by suit, then numberic order


# player.draw(deck)
# player.show_hand()
# print(deck.is_empty())

# Deal out the entire deck of cards
# while not deck.is_empty():
#     player.draw(deck)
#     lazy.draw(deck)
#     smart.draw(deck)
#
# print(deck.is_empty())
# player.show_hand()
# lazy.show_hand()
# smart.show_hand()



#
# bob.draw(deck)
# bob.show_hand()
