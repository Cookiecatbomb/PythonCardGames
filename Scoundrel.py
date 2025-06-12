# going to rename this later to blackguard
# why? because its cool
# also, like "scoundrel" is a synonym of "rouge", "blackguard" is a synonym of "scoundrel"

'''
    To do
- duribility currenty is basing itself off the weapon damage, where it should only start when the first enemy is killed
- remove the enemies

'''


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

'''
def entrance_story(objType,objValue,itteration,roomcount):
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
'''

def interact_story(objType,objValue):
    global hp
    global weapon
    
    if objType == "♡":
        print('You grab the health potion, it heals', objValue ,'points of your health')
        hp += objValue
        if hp > hpMax:
            hp = hpMax
        print(hp)
        
    elif objType == "♢":
        print(weapon)
        if weapon["weaponType"] == "hand":
            print('you pick up the weapon,', objValue ,'damage')
        # duribility, damage, its an actual weapon
        weapon = {
            "duribility" : objValue,
            "damage" : objValue,
            "weaponType" : objType
        }
        print(weapon)

    elif objType == "♣" or objType == "♠":
        # ask for what weapon is used
        if weapon["duribility"] < objValue:
            # this happens when you dont have the required durability to use your weapon; you fight bare handed
            print("balls...")
            # take damage equal to the monster's 
            hp -= objValue
            if hp > hpKill:
                return('complete')
        if weapon["duribility"] > objValue and weapon["duribility"] - 2 <= objValue and weapon["damage"] >= objValue:
            print('you strike the creature down swiftly and deadly')
            # this shows up when the user kills an enemy who:
            #   - has less hp than your damage
            #   - has hp bewteen your weapon durability and two less of it (exc - inc)
            weapon['duribility'] = objValue
            # effective use of your weapon
            # remove enemy
        elif weapon["duribility"] - 3 >= objValue and weapon["damage"] >= objValue:
            print('you wildly chop into the creature')
            # this shows up whan the user kills an enemy who:
            #   - has less hp than your damage
            #   - has less hp than your weapon duribility minus 3 (inc)
            # lackluster use of your weapon
            # remove enemy
        
def start_run():
    global hp
    global weapon
    global hpMax
    global hpKill
    
    MakeDeck()
    print("Deck created...")
    random.shuffle(cards)
    print("loading room...")
    roomCount = 0
    room = cards[:4]
    print('setting weapon...')
    weapon = {
        "duribility" : 0,
        "damage" : 0,
        "weaponType" : "hand"
    }
    print("resetting hp...")
    hp = 20
    hpMax = 20
    hpKill = 0
    print(room)
    card = ''
    '''
    hide:
        # doesnt like to work right now
        # ***definition commented out***
        for encounter in range(len(room)):
            card = room[encounter]
            # encounter was meant to be so that it could go like, "after the room shifts you see x"
            entrance_story(card[-1:],abs(cardvalues[card]),encounter,roomcount)
    '''
    
    """
    hide:
        # just skipping this bit
        if input("is this your fist time? y/n") == "y":
            print("1 - first interaction")
            print("2 - second interaction")
            print("3 - third interaction")
            print("4 - fourth interaction")
            print("0 - reroll interactions (one time in a row)")
            print("Z - restart run")
    """
    
    action = ""
    action 
    while action not in a
    action ctionsLeft:
        action = input('what is your action? ')
        action = action.lower()
    roomContents ={
        "1": room[0],
        "2": room[1],
        "3": room[2],
        "4": room[3]
    }
    if action in roomContents:
        print(f"you chose {roomContents[action]}")
        interact_story(roomContents[action][-1:], abs(cardvalues[roomContents[action]]))
        del roomContents[action]
        print(roomContents)
    if action == "z":
        start_run()
start_run()
