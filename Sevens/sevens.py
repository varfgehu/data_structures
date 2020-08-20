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
            print("pass")
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
        print(self.name + "'s cards:")
        for card in self.hand:
            card.show()

    def organise_hand(self):
        sorted_cards = []
        self.hand.sort()

    def remove_card(self, card):
        self.hand.remove(card)

    def number_of_cards_in_hand(self):
        return len(self.hand)


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
        print("Game players:")
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
            if player == self.head:
                break
        return False

class Layouts(object):
    def __init__(self):
        self.diamonds = []
        self.hearts = []
        self.spades = []
        self.clubs = []

    def show(self):
        suit_lists = [self.diamonds, self.hearts, self.spades, self.clubs]
        suit_dict = {'Hearts': layouts.hearts, 'Diamonds': layouts.diamonds, 'Spades': layouts.spades, 'Clubs': layouts.clubs}
        for suit_name, suit_list in suit_dict.items():
            assemble_list = []
            for suit_item in suit_list:
                assemble_list.append(replace_figures(suit_item))
            print(suit_name, assemble_list)

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



def place_card_to_layout(player, card):
    print("place_card_to_layout")
    print(player.name)
    player.show_hand()
    print("card:")
    card.show()
    print()
    # print(card.suit)
    # print(card.value)
    # TODO!!!!!!!!!!!!!!!!!!!!!!
    # Check is it valid
    # 1, Does the user have the card
    # 2, Dose the card fit in the actual layout
    # Take actions if both are TRUE

    # Check for "pass" / "knock"
    if card is None:
        return
    # remove card from the hand of the player

    player.remove_card(card)
    # add to the layout
    # sort the layout
    layouts.add_card(card)


def return_possible_cards(player):
    possible_cards = []
    dict = {'Hearts': layouts.hearts, 'Diamonds': layouts.diamonds, 'Spades': layouts.spades, 'Clubs': layouts.clubs}

    #for suit_layout in [layouts.diamonds, layouts.hearts, layouts.spades, layouts.clubs]:
    for suit_name, suit_list in dict.items():
        # Find the index in values (2..14) of the firt element ([:1]) of the list, the previous index is a value for a possible card (if in range)
        if len(suit_list) == 0:
            possible_cards.append(Card(suit_name, 7))
            continue

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

    possible_cards = []
    possible_cards = return_possible_cards(player)

    # Print selected cards (DEBUG)
    if len(possible_cards) == 0:
        return "pass"
    print("Suitable cards:")
    for i in range(len(possible_cards)):
        possible_cards[i].show()


    # You have now the available cards for a valid move
    # Now you have to check, if the actual player has any of them.

    num_of_cards = len(possible_cards)
    if num_of_cards == 1:
        return possible_cards[0]
    else:
        # This is where a lazy and smart solutions should be separated

        # This is the lazy solution for now
        for i in range(0, num_of_cards-1):
            if possible_cards[i] in player.hand:
                return possible_cards[i]
        return None



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
    if card_input == "pass" or card_input == "knock":
        return None

    suit_code = card_input[-1]
    if suit_code == "d":
        card_suit = "Diamonds"
    elif suit_code == "h":
        card_suit = "Hearts"
    elif suit_code == "s":
        card_suit = "Spades"
    elif suit_code == "c":
        card_suit = "Clubs"
    else:
        print("Unknown suit code input!")
        return False

    value_code = card_input[:-1]
    if value_code == "a":
        card_value = 14
    elif value_code == "j":
        card_value = 11
    elif value_code == "q":
        card_value = 12
    elif value_code == "k":
        card_value = 13
    else:
        card_value = int(value_code)

    return Card(card_suit, card_value)


def validate_card(player, card):
    """
    Validation steps:
    1, If "pass" was given (None card), check if any of the possible cards is in the player hand
    2, Check if the card entered by the user is in his/her hand
    3, Check if the card is suitable for the layout
    """
    possible_cards = return_possible_cards(player)
    if card is None:
        for possible_card in possible_cards:
            if possible_card in player.hand:
                return False
        return True

    if card not in user.hand:
        return False

    if card not in possible_cards:
        return False

    return True


################################################################################
############################ MAIN ##############################################
################################################################################

# Create the deck of the 52 cards
deck = Deck()
# deck.show()

# Shuffle the cards
deck.shuffle()
print()
players = Players()
player_name = input("Please enter a name!\n")
user = Player(player_name)
lazy = Player("Lazy")
smart  = Player("Smart")
players.append(user)
players.append(lazy)
players.append(smart)
players.show_game()
user_dealer_choice = input("Would you like to be the first dealer? (y/n)\n")
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

lazy.organise_hand()
# lazy.show_hand()
smart.organise_hand()
# smart.show_hand()

user.organise_hand()
# user.show_hand()



# Create layout for the layed down cards
layouts = Layouts()
# layouts.show()

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
        print("\n\nYour turn: " + str(player_with_action.name))
        print("Layout")
        layouts.show()
        player_with_action.show_hand()
        print("Select a card from your hand!\n(Selected card format: For 7 of Diamonds enter 7d, for King of Heart enter kh)\n")
        while True:
            card_input = input("")
            selected_card = generate_card_from_input(card_input)
            if validate_card(player_with_action, selected_card):
                break
    else:
        print(str(player_with_action.name) + "'s turn")
        selected_card = card_selection_magic(player_with_action)

    print(player_with_action.name + "'s action:")
    if selected_card is None:
        print("pass")
    else:
        selected_card.show()
        place_card_to_layout(player_with_action, selected_card)


    if player_with_action.number_of_cards_in_hand() == 0:
        # The current game is over
        # Count points or handle money....
        # Ask user what he/she wants.. ( play again, quit)
        print("The winner is: ", player_with_action.name)
        break

    player_with_action = player_with_action.next

print("Thank you for playing, try again soon!")



































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
