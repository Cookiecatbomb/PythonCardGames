import os
import random
import time


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

tens = ['1','J','Q','K']

# Generate deck
def make_deck():
    for suit in range(1, 5):
        for value in range(1, 14):
            display = ""
            if value == 11:
                display += "Jack"
            elif value == 12:
                display += "Queen"
            elif value == 13:
                display += "King"
            elif value == 1:
                display += "Ace"
            else:
                display += str(value)
            if suit == 1:
                display += " ♡"
            elif suit == 2:
                display += " ♠"
            elif suit == 3:
                display += " ♢"
            elif suit == 4:
                display += " ♣"
            cards.append(display)


def addcards(value, suit):
    cards.append(str(value + ' ' + suit))


def draw(draw):
    global cards
    global drawn_Cards
    for i in range(draw):
        drawn_Cards.append(cards[i])
    cards = cards[draw:]


def House_draw(draw):
    global cards
    global House_cards
    for i in range(draw):
        House_cards.append(cards[i])
    cards = cards[draw:]


def shuffle(refill):
    global cards
    if refill:
        cards = []
        make_deck()
    random.shuffle(cards)


def discard(discard):
    global cards
    cards = cards[discard:]


def print_drawn_cards():
    print('Your cards:')
    for i in range(len(drawn_Cards)):
        print(drawn_Cards[i])
    print()


def print_house_cards():
    print("House's cards:")
    for i in range(len(House_cards)):
        print(House_cards[i])
    print()


def black_jack():
    global cards
    global drawn_Cards
    global House_cards

    def find_player_value(player):
        global playerScore
        global houseScore
        value = 0
        for i in range(len(drawn_Cards)):
            if drawn_Cards[i][:1] in tens:
                # 1 is 10, A is ace
                value += 10
            elif drawn_Cards[i][:1] == 'A':
                if value >= 11:
                    # Having greater than 11 makes ace equal to 1
                    value += 1
                else:
                    value += 11
            else:
                value += int(drawn_Cards[i][:1])
                # This finds the value of the first digit
        if player == "house":
            houseScore = value
        elif player == "player":
            playerScore = value
        return value

    cards = []
    drawn_Cards = []
    House_cards = []
    playerScore = 0
    houseScore = 0
    shuffle(True)
    for _ in range(2):
        cls()
        draw(1)
        print_drawn_cards()
        time.sleep(0.3)
    print(find_player_value("player"))
    while True:
        hitstand = input()
        while hitstand != "h" and hitstand != "s":
            hitstand = input()
        if hitstand == 'h':
            cls()
            if len(cards) > 0:
                draw(1)
                print_drawn_cards()
                print(find_player_value("player"))
            else:
                print("I am out of cards.")
                print(find_player_value("player"))
            if find_player_value("player") >= 21:
                hitstand = "s"
        if hitstand == 's':
            # Houses turn
            for _ in range(2):
                cls()
                House_draw(1)
                print_drawn_cards()
                print(find_player_value("player"))
                print_house_cards()
                print(find_player_value("house"))
                time.sleep(0.3)


playing = True
while playing:
    black_jack()
