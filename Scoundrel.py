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
    for value in range(2, 15):
      display = ""
      if value == 11:
        display += "J"
      elif value == 12:
        display += "Q"
      elif value == 13:
        display += "K"
      elif value == 14:
        display += "A"
      else:
        display += str(value)
      if suit == 1:
        if value >= 11:
            allowed = False
        else:
            allowed = True 
        display += " ♡"
      elif suit == 2:
        display += " ♠"
      elif suit == 3:
         if value >= 11:
            allowed = False
        else:
            allowed = True 
        display += " ♢"
      elif suit == 4:
        display += " ♣"
    if allowed:
      cards.append(display)
      
      
random.shuffle(cardvalues)
print(cardsvalues)
