import os
import random
import time

from readchar import key, readkey


def cls():
  os.system('cls' if os.name == 'nt' else 'clear')


#generate deck
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

  def find_player_value():
    player_value = 0
    for i in range(len(drawn_Cards)):
      if drawn_Cards[i][1:] == '1' or 'J' or 'Q' or 'K':
        player_value += 10
      elif drawn_Cards[i][1:] == 'A':
        if player_value >= 11:
          player_value += 1
        else:
          player_value += 11
      else:
        player_value += int(drawn_Cards[i][1:])

  def find_house_value():
    house_value = 0
    for i in range(len(House_cards)):
      if drawn_Cards[i][1:] == '1' or 'J' or 'Q' or 'K':
        house_value += 10
      elif drawn_Cards[i][1:] == 'A':
        if house_value >= 11:
          house_value += 1
        else:
          house_value += 11
      else:
        house_value += int(House_cards[i][1:])
  
  cards = []
  drawn_Cards = []
  House_cards = []
  shuffle(True)
  for _ in range(2):
    cls()
    draw(1)
    print_drawn_cards()
    time.sleep(0.3)
  find_player_value()
  while True:
    h_s = readkey()
    while h_s != "h" and h_s != "s":
      h_s = readkey()
    if h_s == 'h':
      cls()
      draw(1)
      print_drawn_cards()
      find_player_value()
    elif h_s == 's':
      #houses turn
      for _ in range(2):
        cls()
        House_draw(1)
        print_drawn_cards()
        print_house_cards()
        time.sleep(0.3)
  


playing = True
while playing:
  black_jack()
