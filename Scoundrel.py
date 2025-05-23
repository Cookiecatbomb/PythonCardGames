
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

def EntranceStory(objType,objValue,itteration,roomcount):
    if itteration == 0:
        if roomcount == 0:
            print("You enter the dungeon")
        elif roomcount == 1:
            print('The room shifts...')
    if objType == "♡":
        print('On the floor, you can see a health potion, looks like it could heal', objValue ,'of your hp')
    elif objType == "♢":
        print('Against the wall, you can see a weapon, looks like it could hit for', objValue ,'damage')
    elif objType == "♣" or objType == "♠":
        print('Looking towards you, you see a monster staring you down, looks like it could hit you for', objValue ,'damage')
        
def start_run():
    MakeDeck()
    print("Deck created...")
    random.shuffle(cards)
    print("loading room...")
    roomCount = 0
    room = cards[:4]
    print(room)
    card = ''
    '''
    for encounter in range(len(room)):
        card = room[encounter]
        EntranceStory(card[-1:],abs(cardvalues[card]),encounter,roomcount)
    '''
    if input("is this your fist time? y/n") == "y":
        print("1 - first interaction")
        print("2 - second interaction")
        print("3 - third interaction")
        print("4 - fourth interaction")
        print("0 - reroll interactions")
        print("Z - restart run")
    action = ""
    while action not in ("1","2","3","4","0","Z"):
        action = input('what is your action? ')
    roomContents ={
        "1": room[0],
        "2": room[1],
        "3": room[2],
        "4": room[3]
    }
    if action in roomContents:
        print(roomContents[action])
    if action == "Z":
        start_run()
start_run()
