import random
cards = []
cardvalues = {
'2 ♠': -2, '3 ♠': -3, 
'4 ♠': -4, '5 ♠': -5, 
'6 ♠': -6, '7 ♠': -7, 
'8 ♠': -8, '9 ♠': -9, 
'10 ♠': -10, 'J ♠': -11, 
'Q ♠': -12, 'K ♠': -13, 
'A ♠': -14, 

'2 ♣': -2, '3 ♣': -3, 
'4 ♣': -4, '5 ♣': -5, 
'6 ♣': -6, '7 ♣': -7, 
'8 ♣': -8, '9 ♣': -9, 
'10 ♣': -10, 'J ♣': -11, 
'Q ♣': -12, 'K ♣': -13, 
'A ♣': -14,

'2 ♢': 2, '3 ♢': 3, 
'4 ♢': 4, '5 ♢': 5, 
'6 ♢': 6, '7 ♢': 7, 
'8 ♢': 8, '9 ♢': 9, 
'10 ♢': 10, 

'2 ♡': 2, '3 ♡': 3, 
'4 ♡': 4, '5 ♡': 5, 
'6 ♡': 6, '7 ♡': 7,
'8 ♡': 8, '9 ♡': 9, 
'10 ♡': 10, 
}

for suit in range(1, 5):
    for value in range(1, 14):
      display = ""
      if value == 11:
        display += "J"
      elif value == 12:
        display += "Q"
      elif value == 13:
        display += "K"
      elif value == 1:
        display += "A"
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
      
      
random.shuffle(cardvalues)
print(cardsvalues)
