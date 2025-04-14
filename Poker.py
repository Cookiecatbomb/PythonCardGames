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


def community_draw(draw):
  global cards
  global community_cards
  for i in range(draw):
    community_cards.append(cards[i])
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


def print_commuity_cards():
  print('Community cards:')
  for i in range(len(community_cards)):
    print(community_cards[i])
  print()


def poker():
  global cards
  global drawn_Cards
  global community_cards
  cls()

  def flop():
    cls()
    discard(1)
    for _ in range(3):
      cls()
      community_draw(1)
      print_drawn_cards()
      print_commuity_cards()
      get_hand_type()
      time.sleep(0.3)

  def turn():
    cls()
    discard(1)
    community_draw(1)
    print_drawn_cards()
    print_commuity_cards()
    get_hand_type()

  def river():
    cls()
    discard(1)
    community_draw(1)
    print_drawn_cards()
    print_commuity_cards()
    get_hand_type()

  def fold():
    print('you coward')

  def call():
    bet = prior_bet

  def bet_more():  #raise name wont work
    print("how much more do you want to bet?")
    bet = prior_bet + input()

  def get_hand_type():
    numericalvalue = []
    sortednumericalvalue = []
    numberofvalues = []
    suittype = []
    numberofsuits = []
    for i in range(len(drawn_Cards)):  #getting attributes from players cards
      numericalvalue += drawn_Cards[i][:1]  #gets the number from players cards
      sortednumericalvalue += drawn_Cards[
          i][:1]  #gets the number from players cards
      suittype += drawn_Cards[i][-1:]  #gets the number from player cards
    for i in range(
        len(community_cards)):  #getting attributes from community cards
      numericalvalue += community_cards[
          i][:1]  #gets the number from community cards
      sortednumericalvalue += community_cards[
          i][:1]  #gets the number from community cards #type:ignore
      suittype += community_cards[i][-1:]  #gets the suit from community cards
    for i in range(len(numericalvalue)):  #for each card...
      numberofvalues.append(
          numericalvalue.count(numericalvalue[i])
      )  #...prints how many of each number in play there are #type: ignore
    print()  #line break
    for i in range(len(suittype)):  #for each suit...
      numberofsuits.append(suittype.count(
          suittype[i]))  #...print how many of each suits

    #finding straights

    for i in range(len(sortednumericalvalue)):
      if sortednumericalvalue[i] == '1':
        sortednumericalvalue[i] = 10
      elif sortednumericalvalue[i] == 'J':
        sortednumericalvalue[i] = 11
      elif sortednumericalvalue[i] == 'Q':
        sortednumericalvalue[i] = 12
      elif sortednumericalvalue[i] == 'K':
        sortednumericalvalue[i] = 13
      elif sortednumericalvalue[i] == 'A':
        sortednumericalvalue[i] = 1
        sortednumericalvalue.append(14)
      else:
        sortednumericalvalue[i] = int(sortednumericalvalue[i])
    sortednumericalvalue.sort()
    straightfinder = []
    for i in range(14):  #the following repeats 14 times
      if i + 1 in sortednumericalvalue:  #if the number is in the total set of cards
        straightfinder.append(i + 1)  #add to the list of all the cards
    straightcountdown = 0
    straighted = []
    straight = False
    for i in range(len(straightfinder) -
                   1):  #for the length of the priorly stated list
      if straightfinder[
          i] + 1 in straightfinder:  #if the following value is in the list
        straightcountdown += 1  #add to the countdown
        if straightcountdown == 4:  #if the coundown is equal to four then add the last 5 values to a list #type:ignore
          straighted.append(straightfinder[i] + 1)
          straighted.append(straightfinder[i])
          straighted.append(straightfinder[i] - 1)
          straighted.append(straightfinder[i] - 2)
          straighted.append(straightfinder[i] - 3)
        elif straightcountdown > 4:
          straighted.append(straightfinder[i] +
                            1)  #otherwise add the last card
          straight = True  #if the countdown is greater than 4 then its a straight
      else:
        straightcountdown = 0  #if the countdown gets interupted then the coundown is reset #type:ignore
    straighted.sort()  #sorting the list
    royal = False
    if straight and 14 in straighted:  #if high ace is in the list then it is royal
      royal = True

    #finding a flush

    flush = False
    for i in range(8):  #flush magic that i dont know how it works
      if i + 5 in numberofsuits:
        flush = True

    if numberofsuits.count(7) >= 7 and len(straighted) >= 7 and royal:
      print('royaler flusher')
    elif numberofsuits.count(7) >= 7 and len(straighted) >= 7:
      print('harder, better, straighter, flusher')
    elif numberofvalues.count(5) >= 5 and numberofvalues.count(2) >= 2:
      print('filled house')
    elif numberofsuits.count(7) >= 7:
      print('flusher')
    elif len(straighted) >= 7:
      print('straighter')
    elif numberofvalues.count(5) >= 5 and flush:
      print("flush five(balatro reference)")
    elif numberofvalues.count(2) >= 2 and numberofvalues.count(
        3) >= 3 and flush:
      print("flush house(balatro reference)")
    elif numberofvalues.count(4) >= 4 and numberofvalues.count(3) >= 3:
      print('fuller house')
    elif numberofvalues.count(5) >= 5:
      print("five of a kind(balatro reference)")
    elif flush and straight and royal:
      print("royal flush")
    elif flush and straight:
      print("straight flush")
    elif numberofvalues.count(4) >= 4:
      print("four of a kind")
    elif numberofvalues.count(2) >= 2 and numberofvalues.count(3) >= 3:
      print("full house")
    elif flush:
      print("flush")
    elif straight:
      print("straight")
    elif numberofvalues.count(3) >= 3:
      print("three of a kind")
    elif numberofvalues.count(2) >= 4:
      print("two pair")
    elif numberofvalues.count(2) >= 2:
      print("pair")
    else:
      print("high card")

  cards = []
  drawn_Cards = []
  community_cards = []

  shuffle(True)
  draw(2)
  print_drawn_cards()
  get_hand_type()
  input()
  #betting
  flop()
  input()
  #betting
  turn()
  input()
  #betting
  river()
  input()
  #final bet


playagain = True
while playagain:
  poker()
