
import os
import random
import time

#from readchar import key, readkey
# Not needed?

def cls():
  # Does this even work?
  os.system('cls' if os.name == 'nt' else 'clear')


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
      Cards.append(display)


def add_cards(value, suit):
  # Now this is the cool deck editing software update
  Cards.append(str(value + ' ' + suit))
  # That's it?


def draw(Draw):
  global Cards
  global DrawnCards
  for i in range(Draw):
    DrawnCards.append(Cards[i])
  Cards = Cards[Draw:]


def community_draw(draw):
  # This finds the top "i" cards in the deck and returns it
  global Cards
  global CommunityCards
  for i in range(draw):
    CommunityCards.append(Cards[i])
  Cards = Cards[draw:]


def shuffle(Refill):
  # This uses the random import 
  global Cards
  if Refill:
    Cards = []
    make_deck()
  random.shuffle(Cards)


def discard(Discard):
  # This removes cards directly from the deck
  global Cards
  Cards = Cards[Discard:]


def print_drawn_cards():
  print('Your cards:')
  for i in range(len(DrawnCards)):
    print(DrawnCards[i])
  print()


def print_commuity_cards():
  print('Community cards:')
  for i in range(len(CommunityCards)):
    print(CommunityCards[i])
  print()


def poker():
  global Cards
  global DrawnCards
  global CommunityCards
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
    #bet = PriorBet
    print("hello world")

  def bet_more():  # Raise name won't work
    print("how much more do you want to bet?")
    #bet = PriorBet + input()

  def get_hand_type():
    NumericalValue = []
    SortedNumericalValue = []
    NumberOfValues = []
    suittype = []
    NumberOfSuits = []
    for i in range(len(DrawnCards)):
      # Getting attributes from players cards
      # Gets the number from players cards
      NumericalValue += DrawnCards[i][:1] 
      SortedNumericalValue += DrawnCards[i][:1]
      suittype += DrawnCards[i][-1:]
    for i in range(
        len(CommunityCards)):  
      # Getting attributes from community cards
      # Gets the number from community cards
      NumericalValue += CommunityCards[i][:1]
      SortedNumericalValue += CommunityCards[i][:1]
      # Gets the suit from community cards
      suittype += CommunityCards[i][-1:]
    for i in range(len(NumericalValue)):
      # For each card Prints how many of each number in play there are
      NumberOfValues.append(NumericalValue.count(NumericalValue[i]))  
    print()  # line break
    for i in range(len(suittype)):  # 
      # For each suit print how many of each suits
      NumberOfSuits.append(suittype.count(suittype[i]))
    # Finding straights

    for i in range(len(SortedNumericalValue)):
      if SortedNumericalValue[i] == '1':
        SortedNumericalValue[i] = 10
      elif SortedNumericalValue[i] == 'J':
        SortedNumericalValue[i] = 11
      elif SortedNumericalValue[i] == 'Q':
        SortedNumericalValue[i] = 12
      elif SortedNumericalValue[i] == 'K':
        SortedNumericalValue[i] = 13
      elif SortedNumericalValue[i] == 'A':
        SortedNumericalValue[i] = 1
        SortedNumericalValue.append(14)
      else:
        SortedNumericalValue[i] = int(SortedNumericalValue[i])
    SortedNumericalValue.sort()
    StraightFinder = []
    # The following repeats 14 times
    for i in range(14):
      # If the number is in the total set of cards
      if i + 1 in SortedNumericalValue:
        # Add to the list of all the cards
        StraightFinder.append(i + 1)  
    StraightCountdown = 0
    Straighted = []
    Straight = False
    for i in range(len(StraightFinder) -
                   1):  # For the length of the priorly stated list
      if StraightFinder[i] + 1 in StraightFinder:  # If the following value is in the list
        StraightCountdown += 1  # Add to the countdown
        if StraightCountdown == 4:  # If the countdown is equal to four then add the last 5 values to a list #type:ignore
          Straighted.append(StraightFinder[i] + 1)
          Straighted.append(StraightFinder[i])
          Straighted.append(StraightFinder[i] - 1)
          Straighted.append(StraightFinder[i] - 2)
          Straighted.append(StraightFinder[i] - 3)
        elif StraightCountdown > 4:
          Straighted.append(StraightFinder[i] +
                            1)  # Otherwise add the last card
          Straight = True  # If the countdown is greater than 4 then it's a straight
      else:
        StraightCountdown = 0  # If the countdown gets interrupted then the countdown is reset #type:ignore
    Straighted.sort()  # Sorting the list
    Royal = False
    if Straight and 14 in Straighted:  # If high ace is in the list then it is royal
      Royal = True

    # Finding a flush.
    # Flush magic that I don't know how it works
    Flush = False
    for i in range(8):  
      if i + 5 in NumberOfSuits:
        Flush = True
    # Here comes the super cool logic for hand types
    if NumberOfSuits.count(7) >= 7 and len(Straighted) >= 7 and Royal:
      print('royaler flusher')
    elif NumberOfSuits.count(7) >= 7 and len(Straighted) >= 7:
      print('harder, better, straighter, flusher')
    elif NumberOfValues.count(5) >= 5 and NumberOfValues.count(2) >= 2:
      print('filled house')
    elif NumberOfSuits.count(7) >= 7:
      print('flusher')
    elif len(Straighted) >= 7:
      print('straighter')
    elif NumberOfValues.count(5) >= 5 and Flush:
      print("flush five(balatro reference)")
    elif NumberOfValues.count(2) >= 2 and NumberOfValues.count(
        3) >= 3 and Flush:
      print("flush house(balatro reference)")
    elif NumberOfValues.count(4) >= 4 and NumberOfValues.count(3) >= 3:
      print('fuller house')
    elif NumberOfValues.count(5) >= 5:
      print("five of a kind(balatro reference)")
    elif Flush and Straight and Royal:
      print("royal flush")
    elif Flush and Straight:
      print("straight flush")
    elif NumberOfValues.count(4) >= 4:
      print("four of a kind")
    elif NumberOfValues.count(2) >= 2 and NumberOfValues.count(3) >= 3:
      print("full house")
    elif Flush:
      print("flush")
    elif Straight:
      print("straight")
    elif NumberOfValues.count(3) >= 3:
      print("three of a kind")
    elif NumberOfValues.count(2) >= 4:
      print("two pair")
    elif NumberOfValues.count(2) >= 2:
      print("pair")
    else:
      print("high card")

  Cards = []
  DrawnCards = []
  CommunityCards = []

  shuffle(True)
  draw(2)
  print_drawn_cards()
  get_hand_type()
  input()
  # Betting
  flop()
  input()
  # Betting
  turn()
  input()
  # Betting
  river()
  input()
  # Final bet


PlayAgain = True
while PlayAgain:
  poker()
