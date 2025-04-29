# going to rename this later to blackguard
# why? because its cool


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
def MakeDeck():
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
                allowed = True 
            elif suit == 3:
                if value >= 11:
                    allowed = False
                else:
                    allowed = True 
                display += " ♢"
            elif suit == 4:
                display += " ♣"
                allowed = True 
            if allowed:
                cards.append(display)

def EntranceStory(objType,objValue):
    if objType == "♡":
        print('On the floor, you can see a health potion, looks like it could heal', objValue ,'of your hp')
    elif objType == "♢":
        print('Against the wall, you can see a weapon, looks like it could hit for', objValue ,'damage')
    elif objType == "♣" or objType == "♠":
        print('Looking towards you, you see a monster staring you down, looks like it could hit you for', objValue ,'damage')
        
MakeDeck()
print("Deck created...")
random.shuffle(cards)

print("loading room...")
room = cards[:4]
print(room)
card = ''
for encounter in range(len(room)):
    card = room[encounter]
    EntranceStory(card[-1:],abs(cardvalues[card]))
